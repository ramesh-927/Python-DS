
def sum_an_array(num, target):

    hashmap = {}
    for i, val in enumerate(num):
        diff = target - val
        if diff in hashmap:
            return (hashmap[diff], val)
        hashmap[val] = i
    return [-1, -1]

arr = [1, 2, 3, 10,9,7,5]
target = 15
print(sum_an_array(arr, target))