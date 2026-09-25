"""Audit a project sign-up CSV against a course roster.

The sign-up sheet has one row per 20-minute slot. Teammates enter one name
each and the same project title in adjacent rows. Observers use either row
of a team talk and attend the full presentation.
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
    "Project title",
    "Observer 1",
    "Observer 2",
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
        if row["Slot #"].strip().casefold() == "break":
            if row["Presenter(s)"].strip().casefold() != "no presentations" or row["Project title"] or any(row[column] for column in ("Observer 1", "Observer 2")):
                issues.append(f"schedule row {line}: break row contains a booking")
            continue
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
        title = normalized(row["Project title"])
        observers = tuple(normalized(row[column]) for column in ("Observer 1", "Observer 2") if row[column])
        if not presenter:
            if title or observers:
                issues.append(f"slot {slot}: title or observers entered without a presenter")
            continue
        if ";" in presenter:
            issues.append(f"slot {slot}: enter only one presenter name")
        if not title:
            issues.append(f"slot {slot}: missing project title")
        if len(set(observers)) != len(observers):
            issues.append(f"slot {slot}: observer listed twice")
        for person in (presenter, *observers):
            if person not in roster:
                issues.append(f"slot {slot}: {person!r} is not in the roster")
        bookings[slot] = (start, presenter, title, observers)

    project_by_slot = {slot: slot for slot in bookings}
    slots_by_title: dict[str, list[int]] = defaultdict(list)
    for slot, (_, _, title, _) in bookings.items():
        if title:
            slots_by_title[title].append(slot)
    for title, slots in slots_by_title.items():
        if len(slots) == 1:
            continue
        slots.sort()
        if len(slots) != 2 or slots[1] != slots[0] + 1 or bookings[slots[1]][0] - bookings[slots[0]][0] != timedelta(minutes=20):
            issues.append(f"project {title!r}: team needs exactly two adjacent slots 20 minutes apart")
            continue
        first, second = slots
        project_by_slot[second] = first
        if bookings[first][1] == bookings[second][1]:
            issues.append(f"slots {first}–{second}: teammates must have different names")
        if set(bookings[first][3]) & set(bookings[second][3]):
            issues.append(f"slots {first}–{second}: observer listed in both team slots")

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
