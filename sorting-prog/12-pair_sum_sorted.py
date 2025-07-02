"""
2 Sum In A Sorted Array
Given an array sorted in non-decreasing order and a target number, find the indices of the two values from the array that sum up to the given target number.

Example
{
"numbers": [1, 2, 3, 5, 10],
"target": 7
}
Output:

[1, 3]
Sum of the elements at index 1 and 3 is 7.
"""

def pair_sum_sorted_array(numbers,target):
    left = 0
    right = len(numbers) -1
    while left < right:
        sum = numbers[left] + numbers[right]
        if sum == target:
            return [left, right]
        elif sum > target:
            right -= 1
        else:
            left += 1
    return [-1, -1]

arr = [1, 2, 3, 5, 10]
target = 7
print(pair_sum_sorted_array(arr, target))
