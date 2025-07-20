import heapq

class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def from_(self):
        return self.v

    def to(self):
        return self.w

    def __lt__(self, other):
        return self.weight < other.weight

    def __repr__(self):
        return f"{self.v}->{self.w} ({self.weight})"


class EdgeWeightedDigraph:
    def __init__(self):
        self.graph = {}
        self.vertices = set()

    def add_edge(self, v, w, weight):
        edge = Edge(v, w, weight)
        self.graph.setdefault(v, []).append(edge)
        self.vertices.add(v)
        self.vertices.add(w)

    def get_adj(self, v):
        return self.graph.get(v, [])

    def get_verts(self):
        return self.vertices


class Dijkstra(EdgeWeightedDigraph):
    def __init__(self, graph, source):
        self.edge_to = {}
        self.dist_to = {v: float('inf') for v in graph.get_verts()}
        self.dist_to[source] = 0

        self.pq = [(0, source)]
        visited = set()

        while self.pq:
            _, v = heapq.heappop(self.pq)
            if v in visited:
                continue
            visited.add(v)
            for e in graph.get_adj(v):
                self._relax(e)

    def _relax(self, e):
        v, w = e.from_(), e.to()
        if self.dist_to[w] > self.dist_to[v] + e.weight:
            self.dist_to[w] = self.dist_to[v] + e.weight
            self.edge_to[w] = e
            heapq.heappush(self.pq, (self.dist_to[w], w))

    def path_to(self, v):
        if v not in self.edge_to:
            return []
        path = []
        while v in self.edge_to:
            e = self.edge_to[v]
            path.insert(0, e)
            v = e.from_()
        return path


class BellmanFord(EdgeWeightedDigraph):
    def __init__(self, graph, source):
        self.edge_to = {}
        self.dist_to = {v: float('inf') for v in graph.get_verts()}
        self.dist_to[source] = 0

        for _ in range(len(graph.get_verts()) - 1):
            for v in graph.get_verts():
                for e in graph.get_adj(v):
                    self._relax(e)

        self.has_negative_cycle = False
        for v in graph.get_verts():
            for e in graph.get_adj(v):
                if self.dist_to[e.to()] > self.dist_to[e.from_()] + e.weight:
                    self.has_negative_cycle = True
                    break

    def _relax(self, e):
        v, w = e.from_(), e.to()
        if self.dist_to[w] > self.dist_to[v] + e.weight:
            self.dist_to[w] = self.dist_to[v] + e.weight
            self.edge_to[w] = e

    def path_to(self, v):
        if self.has_negative_cycle or v not in self.edge_to:
            return []
        path = []
        while v in self.edge_to:
            e = self.edge_to[v]
            path.insert(0, e)
            v = e.from_()
        return path
