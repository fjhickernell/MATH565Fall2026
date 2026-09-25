import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from check_project_bookings import audit, parse_start, read_csv


def row(slot, presenter, team_part="", observer1="", observer2=""):
    return {
        "Slot #": str(slot),
        "Date & Time": f"2026-11-23 {9 + (slot - 1) // 3:02d}:{((slot - 1) % 3) * 20:02d}",
        "Presenter(s)": presenter,
        "Team part": team_part,
        "Observer 1": observer1,
        "Observer 2": observer2,
    }


class BookingAuditTests(unittest.TestCase):
    def setUp(self):
        self.roster = [{"Name": name} for name in ("Ada", "Bo", "Cy", "Di")]

    def test_valid_single_bookings(self):
        rows = [
            row(1, "Ada", observer1="Bo", observer2="Cy"),
            row(2, "Bo", observer1="Ada", observer2="Di"),
            row(3, "Cy", observer1="Bo", observer2="Di"),
            row(4, "Di", observer1="Ada", observer2="Cy"),
        ]
        issues, summary = audit(self.roster, rows)
        self.assertEqual([], issues)
        self.assertEqual(("Ada", 1, 2), summary[0])

    def test_flags_duplicate_and_self_observation(self):
        rows = [
            row(1, "Ada", observer1="Ada", observer2="Bo"),
            row(2, "Bo", observer1="Ada", observer2="Ada"),
        ]
        issues, _ = audit(self.roster, rows)
        self.assertTrue(any("own presentation" in issue for issue in issues))
        self.assertTrue(any("observer listed twice" in issue for issue in issues))
        self.assertTrue(any("0 presentation(s)" in issue for issue in issues))

    def test_team_requires_adjacent_rows_and_same_observers(self):
        rows = [
            row(1, "Ada", "1 of 2", "Cy", "Di"),
            row(3, "Bo", "2 of 2", "Cy"),
        ]
        issues, _ = audit(self.roster, rows)
        self.assertTrue(any("adjacent" in issue for issue in issues))

    def test_team_observers_use_distinct_spaces(self):
        rows = [
            row(1, "Ada", "1 of 2", "Cy"),
            row(2, "Bo", "2 of 2", "Di"),
        ]
        issues, _ = audit(self.roster, rows)
        self.assertFalse(any("both team slots" in issue or "observer listed" in issue for issue in issues))
        rows[1]["Observer 2"] = "Cy"
        issues, _ = audit(self.roster, rows)
        self.assertTrue(any("observer listed in both team slots" in issue for issue in issues))

    def test_reads_excel_csv_with_title_rows(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "schedule.csv"
            path.write_text(
                "MATH 565 project presentation sign-up,,,,,\n"
                "All times America/Chicago,,,,,\n"
                "Slot #,Date & Time,Presenter(s),Team part,Observer 1,Observer 2\n"
                "1,11/23/2026 9:00 AM,Ada,,Bo,Cy\n",
                encoding="utf-8-sig",
            )
            rows = read_csv(path, "Slot #")
            self.assertEqual("Ada", rows[0]["Presenter(s)"])
            self.assertEqual(9, parse_start("Mon, Nov 23, 2026 9:00 AM").hour)

    def test_break_rows_are_not_bookable(self):
        break_row = row(2, "No presentations")
        break_row["Slot #"] = "BREAK"
        rows = [row(1, "Ada"), break_row]
        issues, _ = audit(self.roster, rows)
        self.assertFalse(any("integer" in issue for issue in issues))
        break_row["Observer 1"] = "Bo"
        issues, _ = audit(self.roster, rows)
        self.assertTrue(any("break row contains a booking" in issue for issue in issues))


if __name__ == "__main__":
    unittest.main()
