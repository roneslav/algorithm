
import unittest
from lab5.src.max_experience import max_experience

class TestMaxExperienceFunction(unittest.TestCase):
    def test_max_experience_example1(self):
        test_levels = 4
        test_experience = [
            [3, 1],
            [2, 1, 5],
            [1, 3, 2, 1],
            [0, 1, 0, 1, 0]
        ]

        expected_result = 12


        result = max_experience(test_levels, test_experience)

        self.assertEqual(result, expected_result)

    def test_max_experience_example2(self):
        test_levels = 1
        test_experience = [
            [9999]
        ]

        expected_result = 9999

        result = max_experience(test_levels, test_experience)

        self.assertEqual(result, expected_result)

    def test_max_experience_example3(self):
        test_levels = 5
        test_experience = [
            [0],
            [1, 1],
            [0, 0, 0],
            [1, 1, 1, 1],
            [0, 1, 0, 1, 0]
        ]

        expected_result = 3

        result = max_experience(test_levels, test_experience)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
