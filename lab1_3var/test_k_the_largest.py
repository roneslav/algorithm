"""
module: test_k_the_largest
to test a func test_k_the_largest
"""
import unittest

from k_the_largest import k_the_largest  # pylint: disable=import-error


class TestKTheLargest(unittest.TestCase):
    """
    class: TestKTheLargest
    to write a test function
    """

    def test_k_the_largest(self):
        """
        func: test_k_the_largest
        :return: True/False
        """
        array = [15, 7, 22, 9, 36, 2, 42, 18]

        result = k_the_largest(array, 3)
        self.assertEqual(result, (22, 2))

        result = k_the_largest(array, 2)
        self.assertEqual(result, (36, 4))

        result = k_the_largest(array, 0)
        self.assertIsNone(result)

        result = k_the_largest(array, 10)
        self.assertIsNone(result)


