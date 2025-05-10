from typing import List
from collections import Counter


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counted_nums = Counter(nums)

        for item, count in counted_nums.items():
            if count > 1:
                return True
        return False


if __name__ == "__main__":
    test = Solution()
    print(test.hasDuplicate(nums=[1, 2, 3, 3]))
