"""Audit a project sign-up CSV against a course roster.

The sign-up sheet has one row per 20-minute slot. Teammates enter one name
each in adjacent rows marked 1 of 2 and 2 of 2. Repeat each observer on both
rows of a team talk.
"""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path


SCHEDULE_COLUMNS = (
    "Slot #",
    "Date & Time",
    "Presenter(s)",
    "Team part",
    "Observer 1",
    "Observer 2",
    "Observer 3",
)


def normalized(name: str) -> str:
    return " ".join(name.split()).casefold()


def read_csv(path: Path, header_marker: str) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as source:
        raw = list(csv.reader(source))
    header_index = next(
        (index for index, row in enumerate(raw) if header_marker in (cell.strip() for cell in row)),
        None,
    )
    if header_index is None:
        raise ValueError(f"{path}: no {header_marker!r} header found")
    headers = raw[header_index]
    return [
        {key.strip(): (row[index].strip() if index < len(row) else "")
         for index, key in enumerate(headers) if key}
        for row in raw[header_index + 1:]
        if any(value.strip() for value in row)
    ]


def parse_start(value: str) -> datetime:
    for pattern in (
        "%Y-%m-%d %H:%M", "%Y-%m-%d %H:%M:%S",
        "%m/%d/%Y %I:%M %p", "%m/%d/%y %I:%M %p",
        "%a, %b %d, %Y %I:%M %p",
    ):
        try:
            return datetime.strptime(value, pattern)
        except ValueError:
            pass
    raise ValueError(f"invalid Date & Time: {value!r}")


def audit(roster_rows: list[dict[str, str]], rows: list[dict[str, str]]) -> tuple[list[str], list[tuple[str, int, int]]]:
    issues: list[str] = []
    roster: dict[str, str] = {}
    for line, row in enumerate(roster_rows, 2):
        name = row.get("Name", "")
        key = normalized(name)
        if not key:
            issues.append(f"roster row {line}: missing Name")
        elif key in roster:
            issues.append(f"roster row {line}: duplicate Name {name!r}")
        else:
            roster[key] = name

    bookings: dict[int, tuple[datetime, str, str, tuple[str, ...]]] = {}
    presented: dict[str, set[int]] = defaultdict(set)
    observed: dict[str, set[int]] = defaultdict(set)
    seen_slots: set[int] = set()

    for line, row in enumerate(rows, 2):
        missing = [column for column in SCHEDULE_COLUMNS if column not in row]
        if missing:
            issues.append(f"schedule: missing columns {', '.join(missing)}")
            break
        if not row["Slot #"].isdigit():
            issues.append(f"schedule row {line}: Slot # must be an integer")
            continue
        slot = int(row["Slot #"])
        if slot in seen_slots:
            issues.append(f"schedule row {line}: duplicate slot {slot}")
        seen_slots.add(slot)
        try:
            start = parse_start(row["Date & Time"])
        except ValueError as exc:
            issues.append(f"schedule row {line}: {exc}")
            continue

        presenter = normalized(row["Presenter(s)"])
        team_part = row["Team part"]
        observers = tuple(normalized(row[column]) for column in ("Observer 1", "Observer 2", "Observer 3") if row[column])
        if not presenter:
            if team_part or observers:
                issues.append(f"slot {slot}: team or observers entered without a presenter")
            continue
        if ";" in presenter:
            issues.append(f"slot {slot}: enter only one presenter name")
        if team_part not in ("", "1 of 2", "2 of 2"):
            issues.append(f"slot {slot}: invalid Team part {team_part!r}")
        if len(set(observers)) != len(observers):
            issues.append(f"slot {slot}: observer listed twice")
        for person in (presenter, *observers):
            if person not in roster:
                issues.append(f"slot {slot}: {person!r} is not in the roster")
        bookings[slot] = (start, presenter, team_part, observers)

    project_by_slot = {slot: slot for slot in bookings}
    for slot, (start, presenter, team_part, observers) in sorted(bookings.items()):
        if team_part == "1 of 2":
            next_row = bookings.get(slot + 1)
            if not next_row or next_row[2] != "2 of 2" or next_row[0] - start != timedelta(minutes=20):
                issues.append(f"slot {slot}: team needs an adjacent 2 of 2 slot 20 minutes later")
            else:
                project_by_slot[slot + 1] = slot
                if next_row[1] == presenter:
                    issues.append(f"slots {slot}–{slot + 1}: teammates must have different names")
                if set(observers) != set(next_row[3]):
                    issues.append(f"slots {slot}–{slot + 1}: observers must book both team slots")
        elif team_part == "2 of 2":
            previous = bookings.get(slot - 1)
            if not previous or previous[2] != "1 of 2" or start - previous[0] != timedelta(minutes=20):
                issues.append(f"slot {slot}: team needs an adjacent 1 of 2 slot 20 minutes earlier")

    for slot, (_, presenter, _, observers) in bookings.items():
        project = project_by_slot[slot]
        presented[presenter].add(project)
        for person in observers:
            observed[person].add(project)

    for person, watched in observed.items():
        for project in watched & presented[person]:
            issues.append(f"{roster.get(person, person)}: observation of own presentation at slot {project}")

    summary = []
    for key, name in sorted(roster.items(), key=lambda item: item[1].casefold()):
        p_count, o_count = len(presented[key]), len(observed[key])
        summary.append((name, p_count, o_count))
        if p_count != 1 or o_count != 2:
            issues.append(f"{name}: {p_count} presentation(s), {o_count} distinct observation(s); expected 1 and 2")
    return issues, summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("schedule", type=Path, help="CSV export of the sign-up sheet")
    parser.add_argument("roster", type=Path, help="CSV with a Name column containing every enrolled student")
    parser.add_argument("--summary", type=Path, help="write private per-student counts to this CSV")
    args = parser.parse_args()
    roster_rows = read_csv(args.roster, "Name")
    schedule_rows = read_csv(args.schedule, "Slot #")
    issues, summary = audit(roster_rows, schedule_rows)
    if args.summary:
        with args.summary.open("w", newline="", encoding="utf-8") as output:
            writer = csv.writer(output)
            writer.writerow(("Name", "Presentations", "Distinct observations"))
            writer.writerows(summary)
    print(f"Checked {len(summary)} students and {len(schedule_rows)} slot rows.")
    for issue in issues:
        print(f"ISSUE: {issue}")
    if not issues:
        print("All booking quotas and slot rules are satisfied.")
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
