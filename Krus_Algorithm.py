import unittest


class Graph():
    def __init__(self, graph):
        self.graph = graph
        self.vertices = set()
        self.edges = []

    def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])

    def union(self, parent, glubina, x, y):
        x_root = self.find_parent(parent, x)
        y_root = self.find_parent(parent, y)
        if glubina[x_root] < glubina[y_root]:
            parent[x_root] = y_root
        elif glubina[x_root] > glubina[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            glubina[x_root] += 1

    def kruskal_algorithm(self):
        result = []
        i, col = 0, 0
        for vertex in self.graph:
            self.vertices.add(vertex)
            for neighbor, weight in self.graph[vertex]:
                self.edges.append((vertex, neighbor, weight))
        self.edges = sorted(self.edges, key=lambda item: item[2])
        parent = {vertex: vertex for vertex in self.vertices}
        glubina = {vertex: 0 for vertex in self.vertices}
        while col < len(self.vertices) - 1:
            u, v, w = self.edges[i]
            i += 1
            x = self.find_parent(parent, u)
            y = self.find_parent(parent, v)
            if x != y:
                col += 1
                result.append((u, v, w))
                self.union(parent, glubina, x, y)
        return [(str(u), str(v), w) for u, v, w in result]


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.sort = Graph(graph)

    def test_kruskal(self):
        self.assertEqual(self.sort.kruskal_algorithm(),
                         [('1', '3', 1), ('2', '4', 1), ('4', '7', 1), ('1', '2', 2), ('2', '5', 3), ('3', '6', 3)])


graph = {
    '1': [('2', 2), ('3', 1), ('4', 3), ('6', 6)],
    '2': [('1', 2), ('4', 1), ('5', 3)],
    '3': [('1', 1), ('4', 2), ('6', 3)],
    '4': [('1', 3), ('2', 1), ('3', 2), ('7', 1)],
    '5': [('2', 3), ('7', 4)],
    '6': [('1', 6), ('3', 3), ('7', 7)],
    '7': [('4', 1), ('5', 4), ('6', 7)],
}
