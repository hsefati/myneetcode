from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        max_length = 0

        for num in num_set:
            # Only check for the start of a sequence
            if num - 1 not in num_set:
                current = num
                streak = 1

                while current + 1 in num_set:
                    current += 1
                    streak += 1

                max_length = max(max_length, streak)

        return max_length


if __name__ == "__main__":
    test = Solution()
    print(test.longestConsecutive(nums=[2, 20, 4, 10, 3, 4, 5]))
