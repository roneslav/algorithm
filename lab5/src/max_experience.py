def matrix_to_graph(matrix):
    graph = {}

    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            current_node = (i, j)

            if current_node not in graph:
                graph[current_node] = []
            if i + 1 != rows:
                graph[current_node].append((i + 1, j))

                if j + 1 < len(matrix[i + 1]):
                    graph[current_node].append((i + 1, j + 1))

    return graph


def topological_sort(graph, experience):
    def dfs(node, distance):
        visited.add(node)
        if graph.get(node):
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, distance + experience[neighbor[0]][neighbor[1]])

        result.append((node, distance))

    visited = set()
    result = []

    for node in graph:
        if node not in visited:
            dfs(node, experience[node[0]][node[1]])

    return result[::-1]


def max_experience(levels, experience):
    graph = matrix_to_graph(experience)
    top = topological_sort(graph, experience)
    result = -1
    for coord, exp in top:
        if exp > result:
            result = exp
    return result

# test_levels = 4
# test_experience = [
#     [4],
#     [3, 1],
#     [2, 1, 5],
#     [1, 3, 2, 1],
#     [0, 1, 0, 1, 0]
# ]
# graph = matrix_to_graph(test_experience)
#
# # Convert keys in the graph to tuples
# graph = {tuple(k): [tuple(neigh) for neigh in neighbors] for k, neighbors in graph.items()}
#
# sorted_nodes = topological_sort(graph, test_experience)


with open("career.in", "r") as infile:
    levels = int(infile.readline().strip())
    experience = [list(map(int, infile.readline().split())) for _ in range(levels)]

result = max_experience(levels, experience)
# result = max_experience(test_levels, test_experience)

with open("career.out", "w") as outfile:
    outfile.write(str(result))

# print(graph)
# print(sorted_nodes)
print(result)
