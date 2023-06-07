# Write an program with output for Prim's algorithm

import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def prim_algorithm(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        mst_set = [False] * self.V

        key[0] = 0
        parent[0] = -1

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not mst_set[v] and self.graph[u][v] < key[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        minimum_spanning_tree = []
        for i in range(1, self.V):
            minimum_spanning_tree.append((parent[i], i, self.graph[i][parent[i]]))

        return minimum_spanning_tree

    def min_key(self, key, mst_set):
        min_value = sys.maxsize
        min_index = None

        for v in range(self.V):
            if not mst_set[v] and key[v] < min_value:
                min_value = key[v]
                min_index = v

        return min_index


# Example usage
g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

minimum_spanning_tree = g.prim_algorithm()

print("Edges in the Minimum Spanning Tree:")
for u, v, weight in minimum_spanning_tree:
    print(u, "--", v, "\tWeight:", weight)
