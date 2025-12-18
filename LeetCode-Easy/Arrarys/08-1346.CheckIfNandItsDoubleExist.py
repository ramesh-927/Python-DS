"""
Docstring for LeetCode-Easy.Arrarys.8-1346. Check If N and Its Double Exist
Given an array arr of integers, check if there exist two indices i and j such that :
i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]

Example 1:
Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
Example 2:
Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.
Constraints:
2 <= arr.length <= 500
-103 <= arr[i] <= 103
"""
class Solution:
    def checkIfExist(self, arr):
        seen = set()

        for num in arr:
            if num * 2 in seen or (num % 2 == 0 and num // 2  in seen):
                return True
            seen.add(num)
        return False
    
if __name__== "__main__":
    sol = Solution()
    print(sol.checkIfExist([10,2,5,3]))      # True
    print(sol.checkIfExist([3,1,7,11]))      # False

# Brutoforce - O(n²) time (n is list size),
#def checkIfExist(arr):
    #n = len(arr)
    #for i in range(n):
        #for j in range(n):
            #if i != j and arr[i] == 2 * arr[j]:
                #return True
    #return False

# used a hash set to track seen numbers while iterating through the array. For each number, I check 
# if its double or (if even) its half exists in the set before adding it, achieving O(n) time and 
# space.

# For the current number: First, check if its double (num * 2) is already in the book. If yes, that's a match! 
# Also, if the number is even (num % 2 == 0, meaning divisible by 2 with no remainder), check if 
# its half (num // 2) is in the book. If yes, match!