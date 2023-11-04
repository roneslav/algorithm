def flood_fill(matrix, start, replace_color):
    height, width = len(matrix), len(matrix[0])
    target_color = matrix[start[0]][start[1]]

    def is_valid(x, y):
        return 0 <= x < height and 0 <= y < width

    queue = []
    queue.append(start)

    while queue:
        x, y = queue.pop(0)
        if matrix[x][y] == target_color:
            matrix[x][y] = replace_color
            if is_valid(x + 1, y):
                queue.append((x + 1, y))
            if is_valid(x - 1, y):
                queue.append((x - 1, y))
            if is_valid(x, y + 1):
                queue.append((x, y + 1))
            if is_valid(x, y - 1):
                queue.append((x, y - 1))


def create_input_file(file_name):
    with open(file_name, 'w') as f:
        f.write("10,10\n")
        f.write("9, 9\n")
        f.write("D\n")
        data = [
            ['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
            ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'X', 'X', 'X'],
            ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'X', 'X', 'X'],
            ['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'X'],
            ['W', 'R', 'R', 'R', 'R', 'R', 'G', 'X', 'X', 'X'],
            ['W', 'W', 'W', 'R', 'R', 'G', 'G', 'X', 'X', 'X'],
            ['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'X'],
            ['W', 'B', 'B', 'B', 'B', 'R', 'R', 'X', 'X', 'X'],
            ['W', 'B', 'B', 'X', 'B', 'B', 'B', 'B', 'X', 'X'],
            ['W', 'B', 'B', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
        ]
        for row in data:
            f.write(''.join(row) + '\n')


def read_input_file(file_name):
    with open(file_name, 'r') as f:
        lines = f.read().splitlines()
        height, width = map(int, lines[0].split(','))
        start = tuple(map(int, lines[1].split(',')))
        replacement_color = lines[2]
        matrix = [list(line) for line in lines[3:]]
    return height, width, start, replacement_color, matrix


def write_output_file(file_name, matrix):
    with open(file_name, 'w') as f:
        for row in matrix:
            f.write(''.join(row) + '\n')


if __name__ == "__main__":
    input_file = 'input.txt'
    output_file = 'output.txt'

    create_input_file(input_file)

    height, width, start, replacement_color, matrix = read_input_file(input_file)
    flood_fill(matrix, start, replacement_color)

    write_output_file(output_file, matrix)
