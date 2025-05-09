from collections import deque
from typing import Optional, Generator, List, Any

class GeneralTree:

    class Node:
        __slots__ = ('element', 'parent', 'children')

        def __init__(self, element: int) -> None:
            self.element: int = element
            self.parent: Optional['GeneralTree.Node'] = None
            self.children: List['GeneralTree.Node'] = []

        def add_child(self, node: 'GeneralTree.Node') -> None:
            node.parent = self
            self.children.append(node)

        def remove_child(self, node: 'GeneralTree.Node') -> bool:
            if node in self.children:
                self.children.remove(node)
                node.parent = None
                return True
            return False

        def __repr__(self) -> str:
            return f"Node({self.element})"

    def __init__(self) -> None:
        self.root: Optional[GeneralTree.Node] = None
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def __contains__(self, element: Any) -> bool:
        return self._search_node(element, self.root) is not None

    def __iter__(self) -> Generator[int, None, None]:
        yield from self.pre_order()

    def __repr__(self) -> str:
        return f"GeneralTree([{', '.join(str(x) for x in self.breadth_first())}])"

    def add(self, element: int, parent_element: Optional[int] = None) -> bool:
        """
        Adds an element to the tree. If parent_element is None, sets as root (only if tree is empty).
        Returns True if added, False otherwise.
        """
        new_node = GeneralTree.Node(element)
        if parent_element is None:
            if self.root is not None:
                return False
            self.root = new_node
            self._size = 1
            return True

        parent_node = self._search_node(parent_element, self.root)
        if parent_node:
            parent_node.add_child(new_node)
            self._size += 1
            return True
        return False

    def _search_node(self, element: int, node: Optional[Node]) -> Optional[Node]:
        """
        Recursively searches for a node containing 'element'.
        Returns the node or None if not found.
        """
        if node is None:
            return None
        if node.element == element:
            return node
        for child in node.children:
            result = self._search_node(element, child)
            if result:
                return result
        return None

    def breadth_first(self) -> Generator[int, None, None]:
        """Yields elements in breadth-first order."""
        if self.root is None:
            return
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            yield node.element
            for child in node.children:
                queue.append(child)

    def pre_order(self) -> Generator[int, None, None]:
        """Yields elements in pre-order (node, then children)."""
        def _walk(node: Optional[GeneralTree.Node]) -> Generator[int, None, None]:
            if node is None:
                return
            yield node.element
            for child in node.children:
                yield from _walk(child)
        yield from _walk(self.root)

    def post_order(self) -> Generator[int, None, None]:
        """Yields elements in post-order (children, then node)."""
        def _walk(node: Optional[GeneralTree.Node]) -> Generator[int, None, None]:
            if node is None:
                return
            for child in node.children:
                yield from _walk(child)
            yield node.element
        yield from _walk(self.root)

    def level(self, element: int) -> int:
        """
        Returns the level (depth) of the element (root at level 0), or -1 if not found.
        """
        node = self._search_node(element, self.root)
        if node is None:
            return -1
        depth = 0
        while node.parent:
            node = node.parent
            depth += 1
        return depth

    def remove_branch(self, element: int) -> bool:
        """
        Removes the subtree rooted at 'element'.
        Returns True if removal succeeded, False otherwise.
        """
        node = self._search_node(element, self.root)
        if node is None:
            return False
        if node is self.root:
            self.root = None
            self._size = 0
            return True
        parent = node.parent
        if parent and parent.remove_child(node):
            removed_count = self._count_nodes(node)
            self._size -= removed_count
            return True
        return False

    def _count_nodes(self, node: Optional[Node]) -> int:
        """
        Counts nodes in the subtree rooted at 'node'.
        """
        if node is None:
            return 0
        total = 1
        for child in node.children:
            total += self._count_nodes(child)
        return total
