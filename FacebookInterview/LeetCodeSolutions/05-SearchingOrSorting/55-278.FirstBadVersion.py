"""
Docstring for FacebookInterview.LeetCodeSolutions.05-SearchingOrSorting.55-278.FirstBadVersion

You are a product manager and currently leading a team to develop a new product. Unfortunately, the 
latest version of your product fails the quality check. Since each version is developed based on the 
previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes 
all the following ones to be bad.
You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function 
to find the first bad version. You should minimize the number of calls to the API.

Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:
Input: n = 1, bad = 1
Output: 1
Constraints:
1 <= bad <= n <= 231 - 1
"""
def isBadVersion(version: int) -> bool:
    """
    This is a mock function that simulates LeetCode's API.
    Change the BAD_VERSION value to test different cases.
    """
    BAD_VERSION = 4  # <-- Change this number to test different scenarios
    return version >= BAD_VERSION

class Solution:
    def findBadVersion(self, n):
        low, high= 0, n

        while low < high:
            mid = low + (high - low) // 2

            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return low

if __name__ == "__main__":
    sol = Solution()
    test_cases = [5, 10, 1, 1000000000]
    
    for n in test_cases:
        # Temporarily set different bad versions to see different results
        # Here we'll just run with BAD_VERSION = 4 as defined above
        result = sol.findBadVersion(n)
        print(f"For n = {n}, first bad version is: {result}")

# Time Complexity: O(log n) – Logarithmic, meaning steps grow slowly with n.
# Space Complexity: O(1) – Just a few variables, no extra storage.

# For problems where you need to find the "first" or "last" occurrence of something in a sorted, 
# monotonic sequence (like a boundary where things change from one state to another), always choose 
# binary search.

# I used binary search to find the first bad version by repeatedly dividing the search space in half 
# and adjusting the boundaries based on whether the mid version is bad.
# This achieves O(log n) time complexity, making it optimal for large n.