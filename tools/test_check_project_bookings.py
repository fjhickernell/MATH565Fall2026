import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from check_project_bookings import audit, parse_start, read_csv


def row(slot, presenter, team_part="", observer1="", observer2="", observer3=""):
    return {
        "Slot #": str(slot),
        "Date & Time": f"2026-11-23 {9 + (slot - 1) // 3:02d}:{((slot - 1) % 3) * 20:02d}",
        "Presenter(s)": presenter,
        "Team part": team_part,
        "Observer 1": observer1,
        "Observer 2": observer2,
        "Observer 3": observer3,
    }


class BookingAuditTests(unittest.TestCase):
    def setUp(self):
        self.roster = [{"Name": name} for name in ("Ada", "Bo", "Cy", "Di")]

    def test_valid_single_and_team_bookings(self):
        rows = [
            row(1, "Ada", observer1="Bo", observer2="Cy", observer3="Di"),
            row(2, "Bo", observer1="Ada", observer2="Cy", observer3="Di"),
            row(3, "Cy", "1 of 2", "Ada", "Bo"),
            row(4, "Di", "2 of 2", "Ada", "Bo"),
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

    def test_team_observers_book_both_rows(self):
        rows = [
            row(1, "Ada", "1 of 2", "Cy", "Di"),
            row(2, "Bo", "2 of 2", "Cy"),
        ]
        issues, _ = audit(self.roster, rows)
        self.assertTrue(any("both team slots" in issue for issue in issues))

    def test_reads_excel_csv_with_title_rows(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "schedule.csv"
            path.write_text(
                "MATH 565 project presentation sign-up,,,,,\n"
                "All times America/Chicago,,,,,\n"
                "Slot #,Date & Time,Presenter(s),Team part,Observer 1,Observer 2,Observer 3\n"
                "1,11/23/2026 9:00 AM,Ada,,Bo,Cy,Di\n",
                encoding="utf-8-sig",
            )
            rows = read_csv(path, "Slot #")
            self.assertEqual("Ada", rows[0]["Presenter(s)"])
            self.assertEqual(9, parse_start("Mon, Nov 23, 2026 9:00 AM").hour)


if __name__ == "__main__":
    unittest.main()
