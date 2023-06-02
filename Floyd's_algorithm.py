import sys

def floyd_algorithm(graph):
    num_vertices = len(graph)
    dist = [[0] * num_vertices for _ in range(num_vertices)]

    # Initialize the distance matrix with the graph's adjacency matrix
    for i in range(num_vertices):
        for j in range(num_vertices):
            dist[i][j] = graph[i][j]

    # Find the shortest path between all pairs of vertices
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# Example usage
graph = [
    [0, 5, sys.maxsize, 10],
    [sys.maxsize, 0, 3, sys.maxsize],
    [sys.maxsize, sys.maxsize, 0, 1],
    [sys.maxsize, sys.maxsize, sys.maxsize, 0]
]

shortest_paths = floyd_algorithm(graph)

print("Graph:")
for row in graph:
    print(row)

print("\nShortest paths between all pairs of vertices:")
for row in shortest_paths:
    print(row)
