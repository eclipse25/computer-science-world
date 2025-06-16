def insertion_sort(arr):
    for i in range(1, len(arr)):
        insert_value = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > insert_value:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = insert_value

    return arr
