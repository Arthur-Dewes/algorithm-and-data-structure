class TernarySearchTree:
    """
    Ternary Search Tree (TST - Ternary Trie)

    A dictionary data structure optimized for using strings as keys,
    which combines characteristics of Tries and Binary Search Trees.
    Similar to R-link Tries, it stores characters and values in the nodes.

    Representation:
        Each node contains:
        - An associated value (optional).
        - A specific character (c).
        - Three links:
        - left: Points to the subtree that contains all the keys whose next character
            is smaller than the current character c of the node.
        - mid: Points to the subtree that continues the search with the *next* character
            of the key, assuming the current character of the key is equal to the character c of the node.
        - right: Points to the subtree that contains all the keys whose next character
            is greater than the current character c of the node.
        It has 3 null links at each leaf, making it more space-efficient than the R-link Trie for large R.

    Main Operations:
        - Insertion (put): Traverses the TST comparing the current character of the key with the character
        of the current node (x.c). If it is smaller, it goes to the left subtree (keeping the same index in the key);
        if it is larger, it goes to the right subtree (keeping the same index in the key).
        If they are equal, it goes to the mid subtree and advances to the next character of the key.
        
        When the end of the key is reached (through the mid link), the associated value is set in the node.
        - Search (get): Similar to insertion, it traverses the TST comparing the current character
        of the key with the character of the node. The search follows the left, right
        or mid links according to the comparison. The key is found if the search ends
        in a node with the last character of the key and a non-null value. It is not found
        if a null link is encountered or if the node has a null value. The search examines
        only the necessary characters of the key.
        - Cost (typical case): L + ln N character comparisons.
        - Cost (worst case): L + log N character comparisons (with balancing).
        - Character-based operations: Supports efficiently operations like finding
        prefixes, the longest prefix, and searches with wildcards (partial-match searching). Supports ordered dictionary operations.

    Advantages:
        - As fast as hashing for string keys and uses space efficiently.
        - Faster than hashing, especially for missing keys.
        - More space-efficient than R-link Tries for large alphabets.
        - More flexible than red-black BSTs, as it supports character-based operations.
        - Performance can be guaranteed (L + log N in the worst case) with balancing.

    Disadvantages and Considerations:
        - Works only for string keys.

    Applications:
        - Dictionary implementation (symbol tables), being a faster alternative than hashing for string keys.
        - Advanced search, including wildcard searches (partial-match searching).
    """
    class Node:
        def __init__(self, c):
            self.c = c
            self.val = None
            self.left = None
            self.mid = None
            self.right = None

    def __init__(self):
        self.root = None

    def put(self, key, val):
        if not key:
            return
        self.root = self._put(self.root, key, val, 0)

    def _put(self, x, key, val, d):
        c = key[d]
        if x is None:
            x = self.Node(c)
        if c < x.c:
            x.left = self._put(x.left, key, val, d)
        elif c > x.c:
            x.right = self._put(x.right, key, val, d)
        elif d < len(key) - 1:
            x.mid = self._put(x.mid, key, val, d + 1)
        else:
            x.val = val
        return x

    def get(self, key):
        if not key:
            return None
        x = self._get(self.root, key, 0)
        if x is None:
            return None
        return x.val

    def _get(self, x, key, d):
        if x is None:
            return None
        c = key[d]
        if c < x.c:
            return self._get(x.left, key, d)
        elif c > x.c:
            return self._get(x.right, key, d)
        elif d < len(key) - 1:
            return self._get(x.mid, key, d + 1)
        else:
            return x

    def contains(self, key):
        return self.get(key) is not None

    def delete(self, key):
        if key:
            self.root = self._delete(self.root, key, 0)

    def _delete(self, x, key, d):
        if x is None:
            return None
        c = key[d]
        if c < x.c:
            x.left = self._delete(x.left, key, d)
        elif c > x.c:
            x.right = self._delete(x.right, key, d)
        elif d < len(key) - 1:
            x.mid = self._delete(x.mid, key, d + 1)
        else:
            x.val = None

        if x.val is not None or x.left or x.mid or x.right:
            return x
        return None

    def keys(self):
        result = []
        self._collect(self.root, "", result)
        return result

    def _collect(self, x, prefix, result):
        if x is None:
            return
        self._collect(x.left, prefix, result)
        if x.val is not None:
            result.append(prefix + x.c)
        self._collect(x.mid, prefix + x.c, result)
        self._collect(x.right, prefix, result)

    def keysWithPrefix(self, prefix):
        result = []
        x = self._get(self.root, prefix, 0)
        if x is None:
            return result
        if x.val is not None:
            result.append(prefix)
        self._collect(x.mid, prefix, result)
        return result

    def keysThatMatch(self, pattern):
        result = []
        self._match(self.root, "", pattern, 0, result)
        return result

    def _match(self, x, prefix, pattern, d, result):
        if x is None:
            return
        c = pattern[d]
        if c == '.' or c < x.c:
            self._match(x.left, prefix, pattern, d, result)
        if c == '.' or c == x.c:
            if d == len(pattern) - 1:
                if x.val is not None:
                    result.append(prefix + x.c)
            elif d < len(pattern) - 1:
                self._match(x.mid, prefix + x.c, pattern, d + 1, result)
        if c == '.' or c > x.c:
            self._match(x.right, prefix, pattern, d, result)

    def longestPrefixOf(self, s):
        length = 0
        x = self.root
        i = 0
        while x is not None and i < len(s):
            c = s[i]
            if c < x.c:
                x = x.left
            elif c > x.c:
                x = x.right
            else:
                i += 1
                if x.val is not None:
                    length = i
                x = x.mid
        return s[:length]
