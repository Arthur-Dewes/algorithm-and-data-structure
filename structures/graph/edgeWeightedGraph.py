import heapq

class Edge:
    def __init__(self, v, w, weight):
        self.v = v
        self.w = w
        self.weight = weight

    def either(self):
        return self.v

    def other(self, vertex):
        return self.w if vertex == self.v else self.v

    def __lt__(self, other):
        return self.weight < other.weight

    def __eq__(self, other):
        return (self.v == other.v and self.w == other.w or
                self.v == other.w and self.w == other.v) and self.weight == other.weight

    def __hash__(self):
        return hash((min(self.v, self.w), max(self.v, self.w), self.weight))

    def __repr__(self):
        return f"{self.v} - {self.w} ({self.weight})"

class EdgeWeightedGraph:
    def __init__(self):
        self.graph = {}
        self.vertices = set()
        self.edge_set = set()

    def add_edge(self, v, w, weight):
        edge = Edge(v, w, weight)
        self.graph.setdefault(v, []).append(edge)
        self.graph.setdefault(w, []).append(edge)
        self.vertices.update([v, w])
        self.edge_set.add(edge)

    def get_adj(self, v):
        return self.graph.get(v, [])

    def get_verts(self):
        return self.vertices

    def get_edges(self):
        return self.edge_set


class MST:
    def __init__(self, graph):
        self.graph = graph

    def kruskal(self):
        class UnionFind:
            def __init__(self):
                self.parent = {}

            def add(self, x):
                if x not in self.parent:
                    self.parent[x] = x

            def find(self, x):
                while self.parent[x] != x:
                    self.parent[x] = self.parent[self.parent[x]]
                    x = self.parent[x]
                return x

            def union(self, x, y):
                self.parent[self.find(x)] = self.find(y)

        uf = UnionFind()
        for v in self.graph.get_verts():
            uf.add(v)

        mst = []
        total_weight = 0
        edges = sorted(self.graph.get_edges(), key=lambda e: e.weight)

        for e in edges:
            v, w = e.either(), e.other(e.either())
            if uf.find(v) != uf.find(w):
                uf.union(v, w)
                mst.append(e)
                total_weight += e.weight

        return mst, total_weight

    def prim_lazy(self):
        visited = set()
        mst = []
        total_weight = 0

        start = next(iter(self.graph.get_verts()))
        visited.add(start)

        pq = []
        for e in self.graph.get_adj(start):
            heapq.heappush(pq, (e.weight, e))

        while pq and len(visited) < len(self.graph.get_verts()):
            weight, e = heapq.heappop(pq)
            v, w = e.either(), e.other(e.either())

            if v in visited and w in visited:
                continue

            new_vertex = w if v in visited else v
            visited.add(new_vertex)
            mst.append(e)
            total_weight += weight

            for edge in self.graph.get_adj(new_vertex):
                if edge.other(new_vertex) not in visited:
                    heapq.heappush(pq, (edge.weight, edge))

        return mst, total_weight

    def prim_eager(self):
        verts = self.graph.get_verts()
        edge_to = {v: None for v in verts}
        dist_to = {v: float("inf") for v in verts}
        visited = set()

        pq = []
        start = next(iter(verts))
        dist_to[start] = 0
        heapq.heappush(pq, (0, start))

        while pq and len(visited) < len(verts):
            _, v = heapq.heappop(pq)
            if v in visited:
                continue
            visited.add(v)

            for e in self.graph.get_adj(v):
                w = e.other(v)
                if w in visited:
                    continue
                if e.weight < dist_to[w]:
                    edge_to[w] = e
                    dist_to[w] = e.weight
                    heapq.heappush(pq, (e.weight, w))

        mst = [e for e in edge_to.values() if e is not None]
        total_weight = sum(e.weight for e in mst)
        return mst, total_weight
