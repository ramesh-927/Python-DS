def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

arr = [19,18,23,5,7,8,16,13]
sorted_arr = insertion_sort(arr)
print("Sorted array: ", sorted_arr)