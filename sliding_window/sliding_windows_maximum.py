from typing import List
import collections


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val from q ( out of window)
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1

            r += 1

        return output


if __name__ == "__main__":
    test = Solution()
    print(test.maxSlidingWindow(nums=[1, 2, 1, 0, 4, 2, 6], k=3))
