Let’s walk through the algorithm using Example 1: nums = [-1, 0, 1, 2, -1, -4].

Sort the Array:
Original: [-1, 0, 1, 2, -1, -4].
Sorted: [-4, -1, -1, 0, 1, 2].

Iterate Over i:
i = 0: nums[0] = -4
Target: -nums[0] = 4.
left = 1, right = 5.
Check pairs:
nums[1] + nums[5] = -1 + 2 = 1 < 4 → Increment left.
nums[2] + nums[5] = -1 + 2 = 1 < 4 → Increment left.
nums[3] + nums[5] = 0 + 2 = 2 < 4 → Increment left.
nums[4] + nums[5] = 1 + 2 = 3 < 4 → Increment left.
left = 5 → left == right, stop.

No triplets found.

i = 1: nums[1] = -1
Target: -nums[1] = 1.
left = 2, right = 5.
Check pairs:
nums[2] + nums[5] = -1 + 2 = 1 == 1 → Triplet [-1, -1, 2].
Add to result, skip duplicates:
nums[2] == nums[1], so increment left to 3.
nums[5] == nums[5], but no duplicates to skip for right.
nums[3] + nums[5] = 0 + 2 = 2 > 1 → Decrement right.
nums[3] + nums[4] = 0 + 1 = 1 == 1 → Triplet [-1, 0, 1].
Add to result, increment left, decrement right.
left = 4, right = 4 → left == right, stop.
i = 2: nums[2] = -1 (same as nums[1]), skip to avoid duplicates.
i = 3: nums[3] = 0 > 0, break (since remaining numbers are non-negative).
Output: [[-1, -1, 2], [-1, 0, 1]].
Pseudocode

function threeSum(nums):
    result = []
    sort(nums)
    n = length(nums)
    
    for i from 0 to n-3:
        if i > 0 and nums[i] == nums[i-1]:
            continue  // Skip duplicate i
        if nums[i] > 0:
            break  // Early termination
        target = -nums[i]
        left = i + 1
        right = n - 1
        
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                add [nums[i], nums[left], nums[right]] to result
                while left < right and nums[left] == nums[left+1]:
                    left++  // Skip duplicate left
                while left < right and nums[right] == nums[right-1]:
                    right--  // Skip duplicate right
                left++
                right--
            else if current_sum < target:
                left++
            else:
                right--
    
    return result
Explanation of Key Steps in Pseudocode
Sorting: Sorting allows efficient duplicate handling and two-pointer movement.
Outer Loop: Iterate up to n-3 since we need at least three numbers for a triplet.
Duplicate Skip for i: If nums[i] == nums[i-1], skip to avoid duplicate triplets.
Early Termination: If nums[i] > 0, break since the sum of non-negative numbers cannot be zero.
Two-Pointer Logic:
Compute current_sum = nums[left] + nums[right].
If it equals target, record the triplet and skip duplicates for left and right.
Adjust pointers based on whether current_sum is too small or too large.
Result Storage: Store each valid triplet as a list in the result.
Edge Cases Handled
Empty or Small Arrays: If n < 3, return an empty list (implicitly handled since we need three indices).
No Valid Triplets: Example 2 ([0, 1, 1]) returns [] since no triplet sums to zero.
All Zeros: Example 3 ([0, 0, 0]) returns [[0, 0, 0]].
Duplicates: The algorithm skips duplicates at i, left, and right to ensure unique triplets.
Large Numbers: The constraints (-10^5 <= nums[i] <= 10^5) are handled since we’re summing integers, and no overflow occurs in typical programming environments for three numbers.