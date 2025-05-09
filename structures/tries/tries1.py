class TrieSearchTree:
    """
    Trie (or R-links Trie)

    A dictionary data structure optimized for using strings as keys.
    Instead of storing full keys in the nodes as in a binary search tree,
    the Trie stores the characters of the key along the paths from the root to the leaves.
    Each node represents a common prefix and has R children, one for each possible character in the alphabet.

    Representation:
        Each node contains:
        - An associated value (optional), which indicates that the path from the root to this node
        represents a complete key in the dictionary.
        - An array of R references to child nodes. The characters are implicitly defined by the index of the link in the array. For example, a link at index 'a' points to the node representing the prefix extended with 'a'.
        For an alphabet of size R, the array will have R positions.

    Main Operations:
        - Insertion (put): Traverses the Trie following the links corresponding to the characters
        of the key. If a necessary link does not exist (is null), a new node is created at that point. Once the end of the key is reached, the associated value is set at the final node.
        - Search (get): Traverses the Trie following the links corresponding to the characters
        of the key. The key is found if the traversal goes through the entire key and the final node has a non-null value. The key is not found if any required link is null before completing the key, or if the final node has a null value.
        - Cost (typical case): To find a key (hit), all L characters of the key are examined. To not find a key (miss), typically only a few characters are examined (sub-linear).
        - Deletion (delete): Finds the node corresponding to the key and sets its associated value to null. If a node has a null value and all its links are null, it can be recursively removed to save space.
        - Character-based operations:
        - keysWithPrefix(s): Finds all keys in the dictionary that start with the prefix s.
        - longestPrefixOf(s): Finds the longest key in the dictionary that is a prefix of the string s.

    Advantages:
        - Efficient for character-based operations, such as finding prefixes or the longest prefix.
        - Faster than hashing for missing keys in the typical case (only examines necessary characters).
        - More flexible than Binary Search Trees (BSTs) for dictionary operations.

    Disadvantages and Considerations:
        - It can consume a lot of memory, especially for large alphabets (large R), due to the array of links in each node. The space can be sub-linear if there are many short strings with common prefixes.

    Applications:
        - Autocompletion in user interfaces.
        - Search bars and text editors.
        - IP Routing (using longest prefix search).
    """
    def __init__(self, R=256):
        self.R = R

        class Node:
            def __init__(node_self):
                node_self.val = None
                node_self.next = [None] * self.R

        self.Node = Node
        self.root = self.Node()

    def put(self, key, val):
        self.root = self._put(self.root, key, val, 0)

    def _put(self, x, key, val, d):
        if x is None:
            x = self.Node()
        if d == len(key):
            x.val = val
            return x
        c = ord(key[d])
        x.next[c] = self._put(x.next[c], key, val, d + 1)
        return x

    def get(self, key):
        x = self._get(self.root, key, 0)
        if x is None:
            return None
        return x.val

    def _get(self, x, key, d):
        if x is None:
            return None
        if d == len(key):
            return x
        c = ord(key[d])
        return self._get(x.next[c], key, d + 1)

    def contains(self, key):
        return self.get(key) is not None
