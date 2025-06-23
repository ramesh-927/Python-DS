# Selection Sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = [11,24,13,6,16,18,25,9]
s_sort = selection_sort(arr)
print("Sorted array:", s_sort)

