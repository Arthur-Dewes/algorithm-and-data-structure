class Stack:
    class Node:
        def __init__(self, element):
            self.element = element
            self.next = None

    def __init__(self):
        self.top = None
        self.capacity = 0

    def push(self, value):
        new_node = self.Node(value)
        new_node.next = self.top
        self.top = new_node
        self.capacity += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia!")
        self.top = self.top.next
        self.capacity -= 1

    def peek(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia!")
        return self.top.element

    def size(self):
        return self.capacity

    def is_empty(self):
        return self.top is None

    def clear(self):
        self.top = None
        self.capacity = 0
