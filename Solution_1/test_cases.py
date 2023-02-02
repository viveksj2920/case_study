import unittest
from solve import solve

class TestAttendance(unittest.TestCase):

    def test_attendance_1_day(self):
        self.assertEqual(solve(1), "1/2")
    
    def test_attendance_2_days(self):
        self.assertEqual(solve(2), "2/4")

    def test_attendance_3_days(self):
        self.assertEqual(solve(3), "4/8")

    def test_attendance_4_days(self):
        self.assertEqual(solve(4), "7/15")

    def test_attendance_5_days(self):
        self.assertEqual(solve(5), "14/29")
    
    def test_attendance_5_days(self):
        self.assertEqual(solve(6), "27/56")

    def test_attendance_5_days(self):
        self.assertEqual(solve(7), "52/108")

    def test_attendance_5_days(self):
        self.assertEqual(solve(8), "100/208")

    def test_attendance_5_days(self):
        self.assertEqual(solve(9), "193/401")

    def test_attendance_5_days(self):
        self.assertEqual(solve(10), "372/773")

if __name__ == "__main__":
    unittest.main()