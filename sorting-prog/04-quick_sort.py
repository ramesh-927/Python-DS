# QucikSort Algorithem also called In-Place using Lomuto Partition.

''' 
| Case                   | Time       | Space (recursion stack) |
| ---------------------- | ---------- | ----------------------- |
| Best                   | O(n log n) | O(log n)                |
| Average                | O(n log n) | O(log n)                |
| Worst (sorted/reverse) | O(n²)      | O(n)                    |
'''

def quick_sort(arr, low, high):
    if low < high:
        pi = partitation(arr, low ,high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high) 

def partitation(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1

arr = [90,30,50,60,20,80,70]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted: ", arr)
