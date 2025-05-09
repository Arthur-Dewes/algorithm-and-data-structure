def dualPivotQuickSort(arr, low, high):
    
    if low < high:
        
        left_pivot, right_pivot = partition(arr, low, high)
        
        dualPivotQuickSort(arr, low, left_pivot - 1)
        dualPivotQuickSort(arr, left_pivot + 1, right_pivot - 1)
        dualPivotQuickSort(arr, right_pivot + 1, high)
        
def partition(arr, low, high):
    
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
        
    idx_lt_pivot = i = low + 1
    idx_gt_pivot = high - 1
    left_pivot, right_pivot = arr[low], arr[high]
    
    while i <= idx_gt_pivot:
        
        if arr[i] < left_pivot:
            arr[i], arr[idx_lt_pivot] = arr[idx_lt_pivot], arr[i]
            idx_lt_pivot += 1
            
        elif arr[i] >= right_pivot:
            while arr[idx_gt_pivot] > right_pivot and i < idx_gt_pivot:
                idx_gt_pivot -= 1
                
            arr[i], arr[idx_gt_pivot] = arr[idx_gt_pivot], arr[i]
            idx_gt_pivot -= 1
            
            if arr[i] < left_pivot:
                arr[i], arr[idx_lt_pivot] = arr[idx_lt_pivot], arr[i]
                idx_lt_pivot += 1
                
        i += 1
        
    idx_lt_pivot -= 1
    idx_gt_pivot += 1

    arr[low], arr[idx_lt_pivot] = arr[idx_lt_pivot], arr[low]
    arr[high], arr[idx_gt_pivot] = arr[idx_gt_pivot], arr[high]
    
    return idx_lt_pivot, idx_gt_pivot
