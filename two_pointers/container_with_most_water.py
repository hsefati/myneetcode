from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_water = 0

        while left < right:
            # Calculate the area
            height = min(heights[left], heights[right])
            width = right - left
            max_water = max(max_water, height * width)

            # Move the pointer pointing to the smaller height
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_water


if __name__ == "__main__":
    test = Solution()
    print(test.maxArea(height=[1, 7, 2, 5, 4, 7, 3, 6]))
