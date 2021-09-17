
import sys


def dijkstra(graph, start):
    lengths = [float('inf')] * len(graph)
    prevs = [None] * len(graph)
    visited = [False] * len(graph)

    lengths[start] = 0

    for _ in range(len(graph)):
        # Select unvisited node with the smallest length
        current = None
        for node in range(len(graph)):
            if (visited[node] == False) and (current == None or lengths[node] < lengths[current]):
                current = node

        # Mark current as visited
        visited[current] = True

        # Calculate lengths to neighbors
        for neighbor in [node for node in range(len(graph)) if graph[current][node] > 0]:
            if lengths[neighbor] > lengths[current] + graph[current][neighbor]:
                lengths[neighbor] = lengths[current] + graph[current][neighbor]
                # + 1 to convert from index to number
                prevs[neighbor] = current + 1

    return lengths, prevs


graph = None

filename = sys.argv[1]
with open(filename) as file:
    graph_info = [int(i) for i in file.readline().split(' ')]
    graph = [[0] * graph_info[0] for _ in range(graph_info[0])]
    for line in file:
        vertex_info = [int(i) for i in line.split(' ')]
        graph[vertex_info[0] - 1][vertex_info[1] - 1] = vertex_info[2]
        graph[vertex_info[1] - 1][vertex_info[0] - 1] = vertex_info[2]

start = int(input('start = '))
if start < 1 or start > len(graph):
    exit()

print(dijkstra(graph, start - 1))

