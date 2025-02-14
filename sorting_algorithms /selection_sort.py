def selectionSort(data):
    for i in range(0, len(data)):

        tmp = i

        for j in range(i + 1, len(data)):
            if data[j] < data[tmp]:
                tmp = j

        if tmp != i:
            data[i], data[tmp] = data[tmp], data[i]
