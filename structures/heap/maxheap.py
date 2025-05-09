class MaxHeap:
    """
    A MaxHeap class implements a max heap, a complete binary tree where the value of each parent 
    is greater than or equal to the values of its children.

    Notes:
        - The heap uses a list to represent the binary tree, where for a given index k:
            - The left child is located at index 2*k.
            - The right child is located at index 2*k + 1.
            - The parent is located at index k//2.
        - The first element in the list (heap[0]) is a placeholder and is not part of the heap.
        - For a d-ary tree
            - Swim requires log_d(N) comparisons; sink requires d * log_d(N) comparisons.
            - Ideal quantity (sweet spot): d = 4.

    Immutability:
        It is possible to store elements as `tuple` to make them immutable, preventing any 
        modifications after insertion into the heap. This approach ensures the stability of 
        heap elements and is especially useful when you want to avoid accidental changes to 
        the stored values. Ensure that your elements are compatible with tuple conversion 
        (i.e., iterable) before using this approach and change the necessary parts.

    """

    def __init__(self, *args):
        self.heap = [ ' ' ]
        if len(args) > 0:
            self.heap += args[0]

    def add(self, x):
        self.heap.append(x) # Add the new element at the end of the heap
        self._swim(len(self.heap)-1) # Restore heap order by swimming it up

    def _swim(self, k):
        # While not at root and parent is smaller than current
        while k > 1 and self.heap[k//2] < self.heap[k]:
            print("swap", self.heap[k], "and", self.heap[k//2])
            self.heap[k], self.heap[k//2] = self.heap[k//2], self.heap[k] # Swap with parent
            k = k // 2 # Move up to parent index

    def _sink(self, k, limit=None):
        if limit is None:
            limit = len(self.heap) - 1  # Get the index of the last element in the heap
        
        while 2*k <= limit:   # While the node has at least one child
            j = 2*k  # Set j to left child
            if j+1 <= limit and self.heap[j] < self.heap[j+1]: # If right child exists and is bigger
                j += 1  # Move to right child
            if self.heap[k] >= self.heap[j]:  # If parent is larger than or equal to largest child
                break  # Heap property is satisfied, stop sinking
            print("swap", self.heap[k], "and", self.heap[j])
            self.heap[k], self.heap[j] = self.heap[j], self.heap[k]  # Swap parent and child
            k = j  # Move k to child's index and continue

    def get(self):
        res = self.heap[1] # Store the root value (max element)
        print("move", self.heap[len(self.heap)-1], "to top")
        self.heap[1] = self.heap[len(self.heap)-1]  # Replace root with the last element in the heap
        self.heap.pop() # Remove the last element (now duplicated at root)
        self._sink(1) # Restore heap property by sinking the new root
        return res # Return the original max value

    def printh(self, sp=32):
        b = 1 # Base index for the current level
        elem = 1 # Number of elements in the current level
        print(self.heap[1:])
        while True: # Loop until return statement is reached
            print(" "*(sp//2), end="") # Print all heap elements (excluding placeholder at index 0)
            for i in range(b,b+elem): # Iterate through elements in current level
                if i == len(self.heap): # If we've reached the end of the heap
                    print() # Print newline
                    return
                print(self.heap[i]," "*(sp-1),end="") # Print element and spacing
            print() # Print newline after each level
            b += elem # Update base index for next level
            elem *= 2 # Double the number of elements (binary tree property)
            sp //= 2 # Halve the spacing for the next level

    def sort(self):
        N = len(self.heap) - 1

        for k in range(N//2, 0, -1): # bottom-up phase
            self._sink(k)

        while N > 1:  # sortdown phase
            self.heap[1], self.heap[N] = self.heap[N], self.heap[1]
            N -= 1
            self._sink(1, N)
    
    def getData(self): # return the contents of the heap as a list - except position 0
        return self.heap[1:]

    def delMax(self):
        max_value = self.heap[1]  # Get the maximum value (root of the heap)
        self.heap[1], self.heap[-1] = self.heap[-1], self.heap[1]  # Swap root with the last element
        self.heap.pop()  # Remove the last element (which was the max)
        self._sink(1)  # Restore heap order by sinking the new root
        return max_value  # Return the removed maximum value

    def isEmpty(self):
        return len(self.heap) == 1  # True only when there are no real elements


