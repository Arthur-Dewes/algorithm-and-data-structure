from structures.linkedlist.linkedList import LinkedList
from collections import deque

class IntBinaryTree:

    class Node:    
        def __init__(self, element):
            self.father = None
            self.left = None
            self.right = None
            self.element = element

    def __init__(self):
        self.count = 0
        self.root = None

    def clear(self):
        self.count = 0
        self.root = None

    def is_empty(self):
        return self.root is None

    def size(self):
        return self.count

    def get_root(self):
        if self.is_empty():
            raise ValueError("A árvore está vazia")
        return self.root.element

    def _search_node_ref(self, element, target):
        if target is None:
            return None

        if element == target.element:
            return target

        aux = self._search_node_ref(element, target.left)

        if aux is None:
            aux = self._search_node_ref(element, target.right)

        return aux

    def contains(self, element):
        n_aux = self._search_node_ref(element, self.root)
        return n_aux is not None

    def get_parent(self, element):
        n = self._search_node_ref(element, self.root)
        if n is None or n.father is None:
            return None
        return n.father.element

    def set_root(self, element):
        if self.root is None:
            self.root = self.Node(element)
            self.count += 1
            return True
        else:
            self.root.element = element
            return False

    def add_left(self, element, elem_father):
        aux = self._search_node_ref(elem_father, self.root)

        if aux is None or aux.left is not None:
            return False

        n = self.Node(element)
        n.father = aux
        aux.left = n
        self.count += 1
        return True

    def add_right(self, element, elem_father):
        aux = self._search_node_ref(elem_father, self.root)

        if aux is None or aux.right is not None:
            return False

        n = self.Node(element)
        n.father = aux
        aux.right = n
        self.count += 1
        return True

    def count_nodes(self):
        return self._count_nodes_aux(self.root)

    def _count_nodes_aux(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes_aux(node.left) + self._count_nodes_aux(node.right)

    def remove(self, element):
        node_to_remove = self._search_node_ref(element, self.root)

        if node_to_remove is None:
            return False

        if node_to_remove.left is None and node_to_remove.right is None:
            if node_to_remove == self.root:
                self.root = None
            else:
                if node_to_remove.father.left == node_to_remove:
                    node_to_remove.father.left = None
                else:
                    node_to_remove.father.right = None
        elif node_to_remove.left is None or node_to_remove.right is None:
            child = node_to_remove.left if node_to_remove.left is not None else node_to_remove.right

            if node_to_remove == self.root:
                self.root = child
            else:
                if node_to_remove.father.left == node_to_remove:
                    node_to_remove.father.left = child
                else:
                    node_to_remove.father.right = child
            child.father = node_to_remove.father
        else:
            successor = self._find_min(node_to_remove.right)
            node_to_remove.element = successor.element
            self.remove(successor.element)
            return True

        self.count -= 1
        return True

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def height(self):
        return self._height_aux(self.root)

    def _height_aux(self, node):
        if node is None:
            return -1
        left_height = self._height_aux(node.left)
        right_height = self._height_aux(node.right)
        return 1 + max(left_height, right_height)

    def positions_pre(self):
        lista = LinkedList()
        self._positions_pre_aux(self.root, lista)
        return lista

    def _positions_pre_aux(self, node, lista):
        if node is not None:
            lista.add(node.element)
            self._positions_pre_aux(node.left, lista)
            self._positions_pre_aux(node.right, lista)

    def positions_pos(self):
        lista = LinkedList()
        self._positions_pos_aux(self.root, lista)
        return lista

    def _positions_pos_aux(self, node, lista):
        if node is not None:
            self._positions_pos_aux(node.left, lista)
            self._positions_pos_aux(node.right, lista)
            lista.add(node.element)

    def positions_width(self):

        lista = LinkedList()
        if self.is_empty():
            return lista

        queue = deque()
        queue.append(self.root)

        while queue:
            node = queue.popleft()
            lista.add(node.element)

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

        return lista
