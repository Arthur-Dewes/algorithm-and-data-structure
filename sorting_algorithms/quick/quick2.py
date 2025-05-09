def partition(data, l, r):
    q = l
    for j in range(l,r):
        if data[j] <= data[r]:
            data[j], data[q] = data[q], data[j]
            q += 1
    data[r], data[q] = data[q], data[r]
    return q

def quicksort(data, l, r):
    if l < r:
        q = partition(data, l, r)
        quicksort(data, l, q-1)
        quicksort(data, q+1, r)



