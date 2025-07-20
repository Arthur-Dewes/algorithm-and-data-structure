from queue import Queue

class Graph:
    def __init__(self, *args):
        self.graph = {}
        if len(args) == 1:
            self.__readFromFile(args[0])

    def addEdge(self, v, w):
        self.__addToList(v, w)
        self.__addToList(w, v)

    def getAdj(self, v):
        return self.graph[v]

    def getVerts(self):
        return self.graph.keys()

    def __addToList(self, v, w):
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(w)

    def __readFromFile(self, filename):
        with open(filename) as arq:
            for line in arq:
                verts = line.strip().split()
                self.addEdge(verts[0], verts[1])

    def dfs_path(self, s, v):
        marked = {}
        edgeTo = {}

        def dfs(curr):
            marked[curr] = True
            for neighbor in self.getAdj(curr):
                if neighbor not in marked:
                    edgeTo[neighbor] = curr
                    dfs(neighbor)

        dfs(s)

        if v not in marked:
            return None

        path = []
        while v != s:
            path.insert(0, v)
            v = edgeTo[v]
        path.insert(0, s)
        return path

    def bfs_path(self, s, v):
        marked = {}
        edgeTo = {}
        distTo = {}
        queue = Queue()

        marked[s] = True
        distTo[s] = 0
        queue.put(s)

        while not queue.empty():
            curr = queue.get()
            for neighbor in self.getAdj(curr):
                if neighbor not in marked:
                    marked[neighbor] = True
                    edgeTo[neighbor] = curr
                    distTo[neighbor] = distTo[curr] + 1
                    queue.put(neighbor)

        if v not in marked:
            return None

        path = []
        while v != s:
            path.insert(0, v)
            v = edgeTo[v]
        path.insert(0, s)
        return path

    def has_cycle(self):
        visited = set()

        for v in self.getVerts():
            if v not in visited:
                if self.dfs_path(v, None):
                    return True
        return False