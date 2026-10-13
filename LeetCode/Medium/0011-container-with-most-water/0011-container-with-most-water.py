class Solution:
    def maxArea(self, height: list[int]) -> int:
        left_index = 0
        right_index = len(height)-1
        highest = 0
        while left_index < right_index:
            highest = max((right_index-left_index) * (min(height[left_index],height[right_index])),highest)
            
            if height[left_index] < height[right_index]:
                left_index += 1
                continue
            else:
                right_index -= 1
                continue

        return highest

                
                