class LinkedList:
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next
        
        def __str__(self):
            return str(self.value)

    def __init__(self, iterable=None):
        """Inicializa a lista ligada. Se um iterável for fornecido, adiciona os elementos."""
        self.head = None
        self.tail = None
        self.count = 0

        if iterable is not None:
            if hasattr(iterable, '__iter__'):
                for item in iterable:
                    self.add(item)
            else:
                raise TypeError(f'{type(iterable)} is not iterable')

    def add(self, value: int) -> None:
        """Adiciona um novo elemento no final da lista."""
        new_node = self.Node(value)
        self.count += 1
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert(self, value: int, pos: int) -> None:
        """Insere um elemento na posição especificada."""
        if pos < 0 or pos > self.count:
            raise IndexError("Índice fora do intervalo")
        
        new_node = self.Node(value)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            if self.count == 0:
                self.tail = new_node
        else:
            current = self.head
            for _ in range(pos - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            if new_node.next is None:
                self.tail = new_node

        self.count += 1

    def remove(self, value: int) -> None:
        """Remove o primeiro nó com o valor especificado."""
        current = self.head
        prev = None
        while current:
            if current.value == value:
                if prev is None:
                    self.head = current.next
                    if self.head is None:  # Lista vazia após remoção
                        self.tail = None
                else:
                    prev.next = current.next
                    if prev.next is None:
                        self.tail = prev
                self.count -= 1
                return
            prev = current
            current = current.next
        raise ValueError(f'{value} não encontrado na lista')

    def clear(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0

    def reverse(self) -> None:
        prev = None
        current = self.head
        self.tail = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def is_empty(self) -> bool:
        return self.head is None

    def many(self, value: int) -> int:
        """Retorna o número de ocorrências de um valor na lista."""
        count = 0
        current = self.head
        while current:
            if current.value == value:
                count += 1
            current = current.next
        return count

    def __getitem__(self, pos: int) -> slice | int:
        if isinstance(pos, slice): # slice(start, stop, step)
            walk = pos.step if pos.step is not None else 1

            if walk == 0:
                raise ValueError('Step cannot be zero')
            
            if walk > 0:
                begin = pos.start if pos.start is not None else 0
                end = pos.stop if pos.stop is not None else len(self)
            else:
                begin = pos.start if pos.start is not None else len(self) - 1
                end = pos.stop if pos.stop is not None else -1
            
            if begin < 0:
                begin = len(self) + begin

            if end < 0 and pos.stop is not None:
                end = len(self) + end

            part = LinkedList()
            if walk > 0: # __iter__ (lazy evaluation)
                i = 0
                indexes = range(begin, end, walk)
                it = iter(self)
                while i < end:
                    v = next(it)
                    if i in indexes:
                        part.add_no_end(v)
                    i += 1
            else: # __getitem__ 
                for i in range(begin, end, walk):
                    part.add_no_end(self[i])

            return part

        if isinstance(pos, int):
            if pos < 0:
                pos += self.__count
            if pos < 0 or pos >= self.__count:
                raise IndexError('Invalid pos')

            currentNo = self.__head
            for _ in range(pos):
                currentNo = currentNo.next

            return currentNo.value

    def __setitem__(self, pos: int, value: int) -> None:
        if pos < 0:
            pos = len(self) + pos

        if pos < 0 or pos >= self.__count:
            raise IndexError('Invalid pos')

        currentNo = self.__head
        for i in range(pos):
            currentNo = currentNo.next
        
        currentNo.value = value

    def __delitem__(self, pos) -> None:
        if pos < 0: # converte indice negativo em positivo
            pos = len(self) + pos

        if pos < 0 or pos >= self.__count:
            raise IndexError('Invalid pos')
            
        if pos == 0:
            self.head = self.head.next
            if self.head is None:  # Lista vazia após remoção
                self.tail = None
        else:
            current = self.head
            for _ in range(pos - 1):
                current = current.next

            if current.next is None:  # Se removido o último nó
                self.tail = current
            
            current.next = current.next.next
        
        self.count -= 1

    def __reversed__(self) -> 'LinkedList':
        return LinkedList(self)[::-1]

    def __copy__(self) -> 'LinkedList':
        new_list = LinkedList()
        for value in self:
            new_list.add(value)
        return new_list

    def __eq__(self, other) -> bool:
        if not isinstance(other, LinkedList):
            return False
        if len(self) != len(other):
            return False
        for self_value, other_value in zip(self, other):
            if self_value != other_value:
                return False
        return True

    def __contains__(self, value: int) -> bool:
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
        return '[' + ', '.join([str(node) for node in self]) + ']'
    
    def __repr__(self) -> str:
        return f"LinkedList({self})"
