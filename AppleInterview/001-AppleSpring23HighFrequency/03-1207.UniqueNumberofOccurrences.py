"""
Given an array of integers arr, return true if the number of occurrences of each value in the array 
is unique or false otherwise.
Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:
Input: arr = [1,2]
Output: false
Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true 
Constraints:
1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
"""
class Solution:
    def uniqueOccurrences(self, arr):

        count = {}
        for num in arr:
            count[num] = count.get(num, 0) + 1
        return len(count) == len(set(count.values()))

if __name__ == "__main__":
    sol = Solution()
    print(sol.uniqueOccurrences([1,2,2,1,1,3]))       # prints :True
    print(sol.uniqueOccurrences([1,2]))           # prints : False
    print(sol.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))   # prints :True

# Time Complexity: O(n) → we go through the list only once
# Space Complexity: O(n) → in worst case, all elements are unique

# I used a hash map to count the frequency of each number in O(n) time.
# Then I compared the number of unique frequencies using a set — if sizes match, 
# all frequencies are unique.