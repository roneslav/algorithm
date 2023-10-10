import unittest

from lab2.simplify_schedule import simplify_schedule


class TestSimplifySchedule(unittest.TestCase):

    def test_empty_schedule(self):
        schedule = []
        result = simplify_schedule(schedule)
        self.assertEqual(result, [])

    def test_simple_schedule(self):
        schedule = [(0, 1), (2, 3), (4, 5)]
        result = simplify_schedule(schedule)
        self.assertEqual(result, [(0, 1), (2, 3), (4, 5)])

    def test_overlapping_schedule(self):
        schedule = [(0, 1), (1, 3), (2, 4)]
        result = simplify_schedule(schedule)
        self.assertEqual(result, [(0, 4)])

    def test_complex_schedule(self):
        schedule = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
        result = simplify_schedule(schedule)
        self.assertEqual(result, [(0, 1), (3, 8), (9, 12)])


if __name__ == '__main__':
    unittest.main()