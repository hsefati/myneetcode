from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break

            mid = (left + right) // 2
            res = min(nums[mid], res)
            if nums[mid] >= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

        return res


if __name__ == "__main__":
    test = Solution()
    print(test.findMin(nums=[3, 4, 5, 6, 1, 2]))
