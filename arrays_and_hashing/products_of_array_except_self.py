from typing import List
import math


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for idx in range(len(nums)):
            res.append(math.prod(nums[:idx] + nums[idx + 1 :]))

        return res


if __name__ == "__main__":
    test = Solution()
    print(test.productExceptSelf([1, 2, 4, 6]))
