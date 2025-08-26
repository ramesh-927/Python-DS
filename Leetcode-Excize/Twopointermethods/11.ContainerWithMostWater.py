"""
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:
Input: height = [1,1]
Output: 1
"""
#Algorithm Steps : Initialize Two Pointers:
# Set left = 0 (start of the array).
# Set right = n - 1 (end of the array).
# Initialize a variable max_area to store the maximum area found, starting at 0.  Loop Until Pointers Meet:
# While left < right:
# Calculate the current area:
# \text{current\_area} = \min(\text{height}[left], \text{height}[right]) \times (right - left)
# Update max_area if the current area is larger.
# Move the pointer corresponding to the shorter line:
#If height[left] <= height[right], increment left (move left pointer right).
# Otherwise, decrement right (move right pointer left).
# Return the Result:
# After the loop ends (when left >= right), return max_area.

class Solutions:
    def maxArea(self, height):
        left, right  = 0, len(height) - 1
        max_area = 0

        while  left < right:
            width = right - left
            curr_area = min(height[left], height[right]) * width
            max_area = max(max_area, curr_area)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_area

sol = Solutions()
height = [1,8,6,2,5,4,8,3,7]
result = sol.maxArea(height)
print(result)

# Time Complexity: O(n)
# Space Complexity: O(1)