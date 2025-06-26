# easy-to-understand Python implementation of Counting Sort

def count_sort(arr):
    max_val= max(arr)    # Finding the maximum value in the array

    count = [0] * (max_val + 1)  # Initialize count array with zeros

    for num in arr:
        count[num] += 1       # Count occurrences of each element
    
    indx = 0
    for i in range(len(count)):
        while count[i] > 0:
            arr[indx] = i
            indx += 1
            count[i] -= 1
    return arr

arr = [4,6,6,2,4,2,4,8,9,12,18]
print("Original Array: ", arr)

sorted_arr = count_sort(arr)
print("Sorted array:  ", sorted_arr)



