def mergeSort(data: list[int]) -> list[int]:
    """
    This function determines whether the list is broken
    into individual parts
    """
    if len(data) < 2:
        return data

    middle = len(data)//2
    left = mergeSort(data[:middle])
    right = mergeSort(data[middle:])
    merged = merge(left, right)

    return merged

def merge(left, right):
    """
    When left side/right side is empty, 
    It means that this is an individual item and is already sorted.
    """

    # We make sure the right/left side is not empty
    # meaning that it's an individual item and it's already sorted.
    if not len(left):
        return left

    if not len(right):
        return right

    result = []
    leftIndex = 0
    rightIndex = 0
    totalLen = len(left) + len(right)

    while (len(result) < totalLen):

        # Perform the required comparisons and merge the two parts

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