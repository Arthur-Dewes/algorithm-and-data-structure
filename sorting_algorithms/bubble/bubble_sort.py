def bubbleSort(data: list[int]) -> None:
    lenght = len(data)

    for i in range(lenght):
        swapped = False

        for j in range(0, lenght - i - 1):

            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True

        if swapped == False:
            break
