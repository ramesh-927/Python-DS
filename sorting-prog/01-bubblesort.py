# This  is bublesort program

def bubble_sort(arr):
    num = len(arr)
    for i in range(num):
        swapped = False
        for j in range(0, num - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

arr = [13,10,25,6,8,9,28]
k = bubble_sort(arr)
print(k)