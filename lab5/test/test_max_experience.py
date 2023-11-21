# test_max_experience.py

import unittest
from lab5.src.max_experience import max_experience, topological_sort, matrix_to_graph

class TestMaxExperienceFunction(unittest.TestCase):
    def test_max_experience_example1(self):
        levels = 4
        experience = [
            [4],
            [3, 1],
            [2, 1, 5],
            [1, 3, 2, 1],
        ]

        expected_result = 12

        result = max_experience(levels, experience)

        self.assertEqual(result, expected_result)

    def test_max_experience_example2(self):
        levels = 1
        experience = [
            [9999]
        ]

        expected_result = 9999

        result = max_experience(levels, experience)

        self.assertEqual(result, expected_result)

    def test_max_experience_example3(self):
        levels = 5
        experience = [
            [0],
            [1, 1],
            [0, 0, 0],
            [1, 1, 1, 1],
            [0, 1, 0, 1, 0]
        ]

        expected_result = 3

        result = max_experience(levels, experience)

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
