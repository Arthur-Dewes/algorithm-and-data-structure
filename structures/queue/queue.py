class Queue:
    class Node:
        def __init__(self, element):
            self.element = element
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, element):
        new_node = self.Node(element)
        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = self.tail
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError("A fila está vazia!")
        element = self.head.element
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.count -= 1
        return element

    def peek(self):
        if self.is_empty():
            raise RuntimeError("A fila está vazia!")
        return self.head.element

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def clear(self):
        self.head = None
        self.tail = None
        self.count = 0
