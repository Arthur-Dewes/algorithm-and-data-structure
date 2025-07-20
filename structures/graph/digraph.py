from enum import Enum

class Digraph:

    class Mark(Enum):
        WHITE = 0
        GRAY = 1
        BLACK = 2

    def __init__(self, *args):
        self.graph = {}
        if len(args) == 1:
            self.__readFromFile(args[0])

    def __readFromFile(self, filename):
        with open(filename) as arq:
            for line in arq:
                verts = line.strip().split()
                self.addEdge(verts[0], verts[1])

    def addEdge(self, v, w):
        self.__addToList(v, w)

    def __addToList(self, v, w):
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(w)

    def getAdj(self, v):
        return self.graph[v]

    def getVerts(self):
        return self.graph.keys()

    def has_cycle(self):
        marked = {v: self.Mark.WHITE for v in self.getVerts()}

        def dfs(v):
            marked[v] = self.Mark.GRAY
            for w in self.getAdj(v):
                if marked[w] == self.Mark.GRAY:
                    return True
                elif marked[w] == self.Mark.WHITE:
                    if dfs(w):
                        return True
            marked[v] = self.Mark.BLACK
            return False

        for v in self.getVerts():
            if marked[v] == self.Mark.WHITE:
                if dfs(v):
                    return True
        return False

    def topological_sort(self):
        marked = {}
        order = []

        def dfs(v):
            marked[v] = True
            for w in self.getAdj(v):
                if w not in marked:
                    dfs(w)
            order.insert(0, v)

        for v in self.getVerts():
            if v not in marked:
                dfs(v)

        return order
