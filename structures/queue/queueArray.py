class QueueArray:
    def __init__(self):
        self._capacity = 8
        self._fila = [None] * self._capacity
        self._count = 0
        self._primeiro = 0
        self._ultimo = 0

    def enqueue(self, element):
        if self._count == self._capacity:
            self._resize(2 * self._capacity)

        self._fila[self._ultimo] = element
        self._ultimo = (self._ultimo + 1) % self._capacity
        self._count += 1

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError("A fila está vazia!")

        element = self._fila[self._primeiro]
        self._fila[self._primeiro] = None
        self._primeiro = (self._primeiro + 1) % self._capacity
        self._count -= 1
        return element

    def peek(self):
        if self.is_empty():
            raise RuntimeError("A fila está vazia!")
        return self._fila[self._primeiro]

    def is_empty(self):
        return self._count == 0

    def size(self):
        return self._count

    def clear(self):
        self.__init__()

    def _resize(self, new_capacity):
        nova_fila = [None] * new_capacity
        for i in range(self._count):
            nova_fila[i] = self._fila[(self._primeiro + i) % self._capacity]
        self._fila = nova_fila
        self._primeiro = 0
        self._ultimo = self._count
        self._capacity = new_capacity
