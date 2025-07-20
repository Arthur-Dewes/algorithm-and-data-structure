from collections import deque

class FlowEdge:
    def __init__(self, v: int, w: int, capacity: float):
        self.v = v
        self.w = w
        self.capacity = capacity
        self.flow = 0.0

    def from_(self) -> int:
        return self.v

    def to(self) -> int:
        return self.w

    def other(self, vertex: int) -> int:
        if vertex == self.v:
            return self.w
        elif vertex == self.w:
            return self.v
        else:
            raise ValueError("Vértice inválido")

    def residual_capacity_to(self, vertex: int) -> float:
        if vertex == self.w:
            return self.capacity - self.flow
        elif vertex == self.v:
            return self.flow
        else:
            raise ValueError("Vértice inválido")

    def add_residual_flow_to(self, vertex: int, delta: float) -> None:
        if vertex == self.w:
            self.flow += delta
        elif vertex == self.v:
            self.flow -= delta
        else:
            raise ValueError("Vértice inválido")

    def __repr__(self):
        return f"{self.v}->{self.w} | cap: {self.capacity:.1f}, flow: {self.flow:.1f}"


class FlowNetwork:
    def __init__(self, V: int):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def add_edge(self, e: FlowEdge) -> None:
        v, w = e.from_(), e.to()
        self.adj[v].append(e)
        self.adj[w].append(e)

    def get_adj(self, v: int):
        return self.adj[v]


class FordFulkerson:
    def __init__(self, G: FlowNetwork, s: int, t: int):
        self.value = 0.0
        self.edge_to = [None] * G.V
        self.marked = [False] * G.V

        while self._has_augmenting_path(G, s, t):
            bottle = float('inf')
            v = t
            while v != s:
                e = self.edge_to[v]
                bottle = min(bottle, e.residual_capacity_to(v))
                v = e.other(v)

            v = t
            while v != s:
                e = self.edge_to[v]
                e.add_residual_flow_to(v, bottle)
                v = e.other(v)

            self.value += bottle

    def _has_augmenting_path(self, G: FlowNetwork, s: int, t: int) -> bool:
        self.marked = [False] * G.V
        self.edge_to = [None] * G.V

        queue = deque()
        queue.append(s)
        self.marked[s] = True

        while queue:
            v = queue.popleft()
            for e in G.get_adj(v):
                w = e.other(v)
                if not self.marked[w] and e.residual_capacity_to(w) > 0:
                    self.edge_to[w] = e
                    self.marked[w] = True
                    queue.append(w)
            if self.marked[t]:
                break

        return self.marked[t]

    def max_flow(self) -> float:
        return self.value

    def min_cut(self, v: int) -> bool:
        return self.marked[v]

