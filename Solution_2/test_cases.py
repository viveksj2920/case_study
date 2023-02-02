import unittest
from solve import GraduationCeremony

class TestGraduationCeremony(unittest.TestCase):
    def test_solve(self):
        graduation = GraduationCeremony(10)
        result = graduation.solve()
        self.assertEqual(result, "372/773")

        graduation = GraduationCeremony(5)
        result = graduation.solve()
        self.assertEqual(result, "14/29")

if __name__ == '__main__':
    unittest.main()