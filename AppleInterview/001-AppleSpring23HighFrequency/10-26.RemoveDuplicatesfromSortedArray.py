"""
Docstring for AppleInterview.001-AppleSpring23HighFrequency.10-26.RemoveDuplicatesfromSortedArray
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that 
each unique element appears only once. The relative order of the elements should be kept the same.
Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number 
of unique elements k.
The first k elements of nums should contain the unique numbers in sorted order. The remaining elements 
beyond index k - 1 can be ignored.
Custom Judge:
The judge will test your solution with the following code:
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length
int k = removeDuplicates(nums); // Calls your implementation
assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.
Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Constraints:
1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""
class Solution:
    def removeDuplicates(self, nums):

        if not nums:
            return 0
        
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return  slow + 1
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicates([1,1,2]))                # 2
    print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))      # 5

# For removing duplicates from a sorted array in-place, always choose the two-pointer technique. One 
# pointer (slow) builds the unique prefix; the other (fast) scans for new values. It's simple, 
# fast (O(n)), and uses no extra space—perfect for interviews. For unsorted arrays, use a set 
# (but that needs O(n) space).

# I used the two-pointer technique: a "slow" pointer tracks the end of the unique elements, while a 
# "fast" pointer iterates through the array. When a new unique element is found, I advance "slow" 
# and copy it there, achieving O(n) time and O(1) space.