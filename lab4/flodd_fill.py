def find_colour_graph(matrix, position):
    x, y = position
    graph = {(x, y): []}
    queue = [(x, y)]
    color = matrix[x][y]
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    iterations = 0  # Лічильник ітерацій

    while queue:
        cx, cy = queue.pop(0)
        for height, width in moves:
            nx, ny = cx + width, cy + height
            if 0 <= nx < len(matrix[0]) and 0 <= ny < len(matrix) and matrix[ny][nx] == color and (
                    nx, ny) not in graph:
                queue.append((nx, ny))
                graph[(nx, ny)] = []
                graph[(cx, cy)].append((nx, ny))
                graph[(nx, ny)].append((cx, cy))
                iterations += 1  # Збільшуємо кількість ітерацій

    return graph, iterations  # Повертаємо кількість ітерацій

def flood_fill(matrix, position, replace_color, output_file):
    graph, iterations = find_colour_graph(matrix, position)
    for y, x in graph.keys():
        matrix[x][y] = replace_color

    with open(output_file, 'w') as f:
        for row in matrix:
            f.write(''.join(row) + '\n')

    return matrix, iterations  # Повертаємо кількість ітерацій

def main(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.read().splitlines()
        height, width = map(int, lines[0].split(','))
        start = tuple(map(int, lines[1].split(',')))
        replacement_color = lines[2]
        target_color = lines[3]
        matrix = [list(line) for line in lines[4:]]

    print("Original Matrix:")
    for row in matrix:
        print(''.join(row))

    modified_matrix, iterations = flood_fill(matrix, start, replacement_color, output_file)

    print("\nModified Matrix:")
    for row in modified_matrix:
        print(''.join(row))

    print("Number of iterations:", iterations)

if __name__ == "__main__":
    input_file = 'input.txt'
    output_file = 'output.txt'
    main(input_file, output_file)
