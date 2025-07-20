class DualPivotQuickSort:
    def __init__(self, arr):
        self.arr = arr
        
    class Pivot:
        def __init__(self, left, right):
            self.left = left
            self.right = right
            
    def sort(self):
        self._dual_pivot_quicksort(0, len(self.arr) - 1)
    
    def _dual_pivot_quicksort(self, low, high):
        if low >= high:
            return
        
        pivot = self._partition(low, high)
        self._dual_pivot_quicksort(low, pivot.left - 1)
        self._dual_pivot_quicksort(pivot.left + 1, pivot.right - 1)
        self._dual_pivot_quicksort(pivot.right + 1, high)
    
    def _partition(self, low, high):
        if self.arr[low] > self.arr[high]:
            self._swap(low, high)
            
        left_pivot_index = low + 1
        right_pivot_index = high - 1
        iterator = low + 1
        
        while iterator <= right_pivot_index:
            if self.arr[iterator] < self.arr[low]:
                self._swap(iterator, left_pivot_index)
                iterator += 1
                left_pivot_index += 1
            elif self.arr[iterator] > self.arr[high]:
                self._swap(iterator, right_pivot_index)
                right_pivot_index -= 1
            else:
                iterator += 1
                
        self._swap(low, left_pivot_index - 1)
        self._swap(high, right_pivot_index + 1)
        
        return self.Pivot(left_pivot_index - 1, right_pivot_index + 1)
    
    def _swap(self, first_index, second_index):
        if first_index != second_index:
            self.arr[first_index], self.arr[second_index] = self.arr[second_index], self.arr[first_index]
