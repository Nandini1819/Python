graph = {
    0: [1,2],
    1: [0,3,4],
    2: [0,4],
    3: [1],
    4: [1,2]
}
def bfs(start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
    print("BFS Traversal: ",visited)
def dfs(start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(neighbour,visited)
    return visited 
bfs(0)
print("Dfs Traversal:",dfs(0))