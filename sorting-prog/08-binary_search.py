def binary_search_recursive(arr, target, left, right):

    if left > right:
        return -1
    
    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search_recursive(arr, target, left, mid -1)
    else:
        return binary_search_recursive(arr,target, mid +1, right)
    

arr = [1, 3, 5, 7, 9, 11, 13]
target = 11
result = binary_search_recursive(arr, target, 0, len(arr) - 1)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")



    
