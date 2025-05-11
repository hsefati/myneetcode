from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        sorted_frequency = sorted(frequency.items(), key=lambda kv: kv[1], reverse=True)
        return [num for num, freq in sorted_frequency[:k]]


if __name__ == "__main__":
    test = Solution()
    print(test.topKFrequent(nums=[1, 2, 2, 3, 3, 3], k=2))
