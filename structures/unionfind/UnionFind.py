class QuickFindUF:
    def __init__(self, N):
        self.id = list(range(N))

    def find(self, p):
        return self.id[p]

    def union(self, p, q):
        pid = self.id[p]
        qid = self.id[q]
        for i in range(len(self.id)):
            if self.id[i] == pid:
                self.id[i] = qid

class QuickUnionUF:
    def __init__(self, N):
        self.id = list(range(N))

    def find(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        self.id[i] = j

class WeightedQuickUnionUF:
    def __init__(self, N):
        self.id = list(range(N))
        self.sz = [1] * N

    def find(self, i):
        while i != self.id[i]:
            # Path compression (path halving)
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        if i == j:
            return
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]
