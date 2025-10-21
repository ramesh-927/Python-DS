def bucket_sort(arr):
    if len(arr) == 0:
        return arr
    
    num_buckets = len(arr)
    buckets =  [[] for _ in range(num_buckets)]

    for num in arr:
        index = int(num * num_buckets)
        buckets[index].append(num)
    
    for buck in buckets:
        buck.sort()

    sorted_array = []
    for buck in buckets:
        sorted_array.extend(buck)
    return sorted_array

arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
sorted_arr = bucket_sort(arr)
print("Sorted array:", sorted_arr)
