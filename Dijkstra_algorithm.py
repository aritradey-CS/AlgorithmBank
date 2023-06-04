import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def dijkstra_algorithm(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        shortest_path_set = [False] * self.V

        for _ in range(self.V):
            u = self.min_distance(dist, shortest_path_set)
            shortest_path_set[u] = True

            for v in range(self.V):
                if (
                    self.graph[u][v] > 0
                    and not shortest_path_set[v]
                    and dist[v] > dist[u] + self.graph[u][v]
                ):
                    dist[v] = dist[u] + self.graph[u][v]

        return dist

    def min_distance(self, dist, shortest_path_set):
        min_value = sys.maxsize
        min_index = None

        for v in range(self.V):
            if not shortest_path_set[v] and dist[v] < min_value:
                min_value = dist[v]
                min_index = v

        return min_index


# Example usage
g = Graph(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 7, 8)
g.add_edge(1, 2, 8)
g.add_edge(1, 7, 11)
g.add_edge(2, 3, 7)
g.add_edge(2, 8, 2)
g.add_edge(2, 5, 4)
g.add_edge(3, 4, 9)
g.add_edge(3, 5, 14)
g.add_edge(4, 5, 10)
g.add_edge(5, 6, 2)
g.add_edge(6, 7, 1)
g.add_edge(6, 8, 6)
g.add_edge(7, 8, 7)

source_vertex = 0
shortest_distances = g.dijkstra_algorithm(source_vertex)

print("Shortest distances from source vertex", source_vertex, ":")
for v in range(g.V):
    print("Vertex", v, "\tDistance:", shortest_distances[v])
