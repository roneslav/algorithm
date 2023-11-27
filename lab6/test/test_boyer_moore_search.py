import unittest

from lab6.src.boyer_moore_search import boyer_moore_search


class TestBoyerMooreSearch(unittest.TestCase):
    def test_simple_case(self):
        haystack = "ababcababcabcabc"
        needle = "abc"
        result = boyer_moore_search(haystack, needle)
        self.assertEqual(result, [2, 7, 10, 13])

    def test_no_match(self):
        haystack = "abababababab"
        needle = "xyz"
        result = boyer_moore_search(haystack, needle)
        self.assertEqual(result, [])

    def test_multiple_occurrences(self):
        haystack = "abababababab"
        needle = "aba"
        result = boyer_moore_search(haystack, needle)
        self.assertEqual(result, [0, 2, 4, 6, 8])

    def test_empty_needle(self):
        haystack = "abababababab"
        needle = ""
        result = boyer_moore_search(haystack, needle)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
