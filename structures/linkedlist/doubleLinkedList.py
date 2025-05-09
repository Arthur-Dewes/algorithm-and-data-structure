class DoubleLinkedList:
    class Node:
        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

        def __str__(self):
            return str(self.value)

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        self.count = 0

        if iterable is not None:
            if hasattr(iterable, '__iter__'):
                for item in iterable:
                    self.add(item)
            else:
                raise TypeError(f'{type(iterable)} is not iterable')

    def add(self, value):
        new_node = self.Node(value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.count += 1

    def insert(self, value, pos):
        if pos < 0 or pos > self.count:
            raise IndexError("Index out of range")
        
        new_node = self.Node(value)
        
        if self.count == 0:
            self.head = self.tail = new_node
        elif pos == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        elif pos == self.count:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            current = self._get_node(pos)
            prev = current.prev
            prev.next = new_node
            new_node.prev = prev
            new_node.next = current
            current.prev = new_node

        self.count += 1

    def remove(self, value):
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                self.count -= 1
                return
            current = current.next
        raise ValueError(f'{value} not found in list')

    def clear(self):
        self.head = self.tail = None
        self.count = 0

    def reverse(self):
        current = self.head
        self.tail = self.head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            current.prev = next_node
            prev = current
            current = next_node
        self.head = prev

    def is_empty(self):
        return self.count == 0

    def many(self, value):
        """Retorna o número de ocorrências de um valor na lista."""
        current = self.head
        total = 0
        while current:
            if current.value == value:
                total += 1
            current = current.next
        return total

    def _get_node(self, pos):
        if pos < 0 or pos >= self.count:
            raise IndexError("Index out of range")
        if pos < self.count // 2:
            current = self.head
            for _ in range(pos):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.count - 1, pos, -1):
                current = current.prev
        return current

    def __getitem__(self, pos):
        if isinstance(pos, slice):
            step = pos.step if pos.step is not None else 1
            if step == 0:
                raise ValueError("Step cannot be zero")

            start = pos.start if pos.start is not None else (0 if step > 0 else self.count - 1)
            stop = pos.stop if pos.stop is not None else (self.count if step > 0 else -1)

            if start < 0:
                start += self.count
            if stop < 0:
                stop += self.count

            sliced = DoubleLinkedList()
            if step > 0:
                i = 0
                current = self.head
                while current and i < stop:
                    if i >= start and (i - start) % step == 0:
                        sliced.add(current.value)
                    current = current.next
                    i += 1
            else:
                i = self.count - 1
                current = self.tail
                while current and i > stop:
                    if i <= start and (start - i) % abs(step) == 0:
                        sliced.add(current.value)
                    current = current.prev
                    i -= 1
            return sliced

        if isinstance(pos, int):
            if pos < 0:
                pos += self.count
            return self._get_node(pos).value

    def __setitem__(self, pos, value):
        if pos < 0:
            pos += self.count
        self._get_node(pos).value = value

    def __delitem__(self, pos):
        if pos < 0:
            pos += self.count
        node = self._get_node(pos)
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        self.count -= 1

    def __reversed__(self):
        reversed_list = DoubleLinkedList()
        current = self.tail
        while current:
            reversed_list.add(current.value)
            current = current.prev
        return reversed_list

    def __copy__(self):
        new_list = DoubleLinkedList()
        for value in self:
            new_list.add(value)
        return new_list

    def __eq__(self, other):
        if not isinstance(other, DoubleLinkedList):
            return False
        if len(self) != len(other):
            return False
        for a, b in zip(self, other):
            if a != b:
                return False
        return True

    def __contains__(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __len__(self):
        return self.count

    def __str__(self):
        return '[' + ', '.join(str(v) for v in self) + ']'

    def __repr__(self):
        return f"DoubleLinkedList({list(self)})"
