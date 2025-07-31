import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left, right = 1, max(piles)
        min_k = max(piles)

        while left <= right:
            k = (left + right) // 2
            possible_min_hour = sum(math.ceil(float(num) / k) for num in piles)
            if possible_min_hour <= h:
                right = k - 1
                min_k = k
            else:
                left = k + 1

        return min_k


if __name__ == "__main__":
    test = Solution()
    print(test.minEatingSpeed(piles=[1, 4, 3, 2], h=9))
