import random

def quicksort(data: list[int], left: int, right: int) -> None:
    if left == 0 and right == len(data) - 1:
        random.shuffle(data)
    
    if left < right:
        pi = partition(data, left, right)
        quicksort(data, left, pi - 1)
        quicksort(data, pi + 1, right)

def partition(data: list[int], left: int, right: int) -> int:
    pivot = data[len(data) // 2]
    i = left - 1
    data[right], data[len(data) // 2] = data[len(data) // 2], data[right] # Moves the pivot to the end

    for j in range(left, right):
        if data[j] <= pivot:
            i = i + 1
            data[i], data[j] = data[j], data[i] # Swaps smaller elements with larger ones

    data[i + 1], data[right] = data[right], data[i + 1] # Moves the pivot to its correct position
    return i + 1 # Returns the pivot position

