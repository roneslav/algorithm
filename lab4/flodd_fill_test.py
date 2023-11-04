import unittest
from flood_fill import flood_fill, create_input_file, read_input_file, write_output_file


class TestFloodFill(unittest.TestCase):
    def setUp(self):
        self.input_file = 'input.txt'
        self.output_file = 'output.txt'

    def test_read_input_file(self):
        input_data = [
            '10,10',
            '8, 7',
            'V',
            'YYYGGGGGGG',
            'YYYYYYGXXX',
            'GGGGGGGXXX',
            'WWWWWWGGGG',
            'WRRRRGGXXX',
            'WWWWGGGGGG',
            'WWBWWRRRRX',
            'WWBWWWXXXB',
            'WWBWWWWWWX'
        ]
        with open(self.input_file, 'w') as f:
            f.write('\n'.join(input_data))

        height, width, start, replacement_color, matrix = read_input_file(self.input_file)

        self.assertEqual(height, 10)
        self.assertEqual(width, 10)
        self.assertEqual(start, (8, 7))
        self.assertEqual(replacement_color, 'V')

if __name__ == '__main__':
    unittest.main()
