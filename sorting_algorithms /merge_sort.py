def mergeSort(data: list[int]) -> list[int]:
    """This function determines whether the list is broken
        into individual parts"""
    if len(data) < 2:
        return data

    middle = len(data)//2
    left = mergeSort(data[:middle])
    right = mergeSort(data[middle:])
    merged = merge(left, right)

    return merged

def merge(left, right):
    """When left side/right side is empty, 
    It means that this is an individual item and is already sorted."""

    #We make sure the right/left side is not empty
    #meaning that it's an individual item and it's already sorted.
    if not len(left):
        return left

    if not len(right):
        return right

    result = []
    leftIndex = 0
    rightIndex = 0
    totalLen = len(left) + len(right)

    #
    while (len(result) < totalLen):

        #Perform the required comparisons and merge the two parts

        if left[leftIndex] < right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1

        if leftIndex == len(left) or rightIndex == len(right):
            result.extend(left[leftIndex:] or right[rightIndex:])

            break

    return result

# MergeSort in Python


def mergeSort2(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

def merge_sort(l:list):
    arr = l[::]
    if len(arr) < 2:
        return arr
    mid = len(arr)//2;
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))

def merge2(l, r):
    arr = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            arr.append(l[i])
            i += 1
        else:
            arr.append(r[j])
            j += 1
    while i < len(l):
        arr.append(l[i])
        i += 1
    while j < len(r):
        arr.append(r[j])
        j += 1
    return arr