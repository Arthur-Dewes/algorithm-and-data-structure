import heapq
from collections import Counter

class HuffmanCoder:
    """
    Implements Huffman coding and decoding for lossless data compression.

    Generates the Huffman tree for encoding symbols based on their frequencies.

    Steps of the Huffman algorithm:
    1. Create a tree for each symbol, with its associated frequency.
    2. Insert all trees into a priority queue (heap), ordered by frequency.
    3. While there is more than one tree in the queue:
        a. Remove the two trees with the lowest frequency.
        b. Create a new tree with these two as children.
        c. The frequency of the new tree is the sum of the two removed.
        d. Insert the new tree back into the queue.
    4. The last remaining tree represents the complete Huffman tree.
    5. To generate the binary codes:
        a. Traverse the tree from the root to the leaves.
        b. Assign '0' when going left and '1' when going right.
        c. The path taken to each leaf defines the binary code of the corresponding symbol.

    This encoding results in shorter codes for more frequent symbols,
    generating efficient compression without loss of information.

    Methods:
    - encode(text): Encodes a string into a binary sequence using Huffman.
    - decode(encoded): Decodes a binary string back into the original text.

    """
    class Tree:
        def __init__(self, ch, freq, left=None, right=None):
            self.ch = ch
            self.freq = freq
            self.left = left
            self.right = right

        def __lt__(self, other):
            return self.freq < other.freq
        
    def __init__(self):
        self.root = None
        self.encoding_map = {}

    def _build_tree(self, text):
        """
        Builds a Huffman tree based on the frequencies of the characters in the given text.

        Parameters:
            text (str): Input text for which the Huffman tree will be built.

        Side effects:
            sets the `self.root` attribute to the root of the generated tree.
        """
        counter = Counter(text)
        pq = [self.Tree(ch, freq) for ch, freq in counter.items()]
        heapq.heapify(pq)

        while len(pq) > 1:
            left = heapq.heappop(pq)
            right = heapq.heappop(pq)
            parent = self.Tree(None, left.freq + right.freq, left, right)
            heapq.heappush(pq, parent)

        self.root = pq[0] if pq else None

    def _build_map(self):
        """
        Generates the encoding dictionary (character-to-bit map) from the Huffman tree.

        Precondition:
            the Huffman tree (self.root) must have been constructed before the call.

        Side effects:
            fills the `self.encoding_map` attribute with the binary codes of the characters.
        """
        def dfs(node, path):
            if node.ch is not None:
                self.encoding_map[node.ch] = ''.join(path)
            else:
                path.append('0')
                dfs(node.left, path)
                path.pop()
                path.append('1')
                dfs(node.right, path)
                path.pop()

        if self.root:
            dfs(self.root, [])

    def encode(self, text: str):
        """
        Encodes a text into a binary sequence using Huffman coding.

        Parameters:
            text (str): Input text to be encoded.

        Returns:
            str: String with the bits ('0' and '1') representing the encoded text.
        """
        self.build_tree(text)
        self.build_map()
        return ''.join(self.encoding_map[ch] for ch in text)

    def decode(self, encoded: str):
        """
        Decodes a binary string back to the original text, based on the generated Huffman tree.

        Parameters:
            encoded(str): Sequence of bits ('0' and '1') representing the encoded text.

        Returns:
            str: Original decoded text.
        """
        if not self.root:
            return ""

        if self.root.ch is not None:
            return self.root.ch * len(encoded)

        decoded = []
        node = self.root
        for bit in encoded:
            node = node.left if bit == '0' else node.right
            if node.ch is not None:
                decoded.append(node.ch)
                node = self.root
        return ''.join(decoded)
