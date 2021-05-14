
def _DFS(G, current, goal, visited):
    if current == goal:
        return [current]

    for neighbor in [i for i in range(len(G)) if G[current][i] == 1]:
        if neighbor not in visited:
            visited.add(neighbor)
            path = _DFS(G, neighbor, goal, visited)

            if path is not None:
                path.insert(0, current)
                return path

    return None


# Пошук в глибину не гарантує знайти найкоротший шлях.
# Для цього його потрібно модифікувати (наприклад IDDFS) або використати пошук в ширину.
def DFS(G, start, goal):
    if start < 1 or start > len(G) or goal < 1 or goal > len(G):
        return False

    start, goal = start - 1, goal - 1
    visited = set()
    visited.add(start)
    path = _DFS(G, start, goal, visited)

    if path is not None:
        return [i + 1 for i in path]
    return False


G = [[0, 1, 0, 0, 1, 0, 0, 0, 0],
     [1, 0, 1, 1, 1, 1, 0, 0, 0],
     [0, 1, 0, 0, 1, 0, 0, 0, 0],
     [0, 1, 0, 0, 1, 0, 1, 1, 0],
     [1, 1, 1, 1, 0, 1, 1, 0, 1],
     [0, 1, 0, 0, 1, 0, 0, 1, 1],
     [0, 0, 0, 1, 1, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 1, 0, 0, 1],
     [0, 0, 0, 0, 1, 1, 0, 1, 0]]

A = int(input('A = '))
B = int(input('B = '))

print(DFS(G, A, B))
