"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute 
how much water it can trap after raining.
Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.
Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
Constraints:
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""
class Solution:
    def trapRainWater(self, height):
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                water += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                right -= 1

        return water
    
if __name__== "__main__":
    sol = Solution()
    print(sol.trapRainWater([0,1,0,2,1,0,1,3,2,1,2,1]))            # Output  : 6
    print(sol.trapRainWater([4,2,0,3,2,5]))                       # Output  : 9
  
# "We use two pointers starting from both ends.At each step we move the pointer with the smaller 
# height, because the water level is bounded by the shorter wall.
# While moving, we keep track of the maximum height seen on each side and add trapped 
# water accordingly."

# Time Complexity : O(n)
# Space Complexity : O(1)

