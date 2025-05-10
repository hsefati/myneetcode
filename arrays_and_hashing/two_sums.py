from typing import List


class SolutionV2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # value -> index
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], idx]
            seen[num] = idx


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, item in enumerate(nums):
            look_for = target - item
            if look_for in nums[idx+1:]:
                look_for_idx = nums[idx+1:].index(look_for)
                return [idx, look_for_idx+idx+1]
            elif look_for in nums[:idx]:
                look_for_idx = nums[:idx].index(look_for)
                return [idx, look_for_idx]
            



if __name__ == "__main__":
    test = SolutionV2()
    print(test.twoSum(nums=[2,5,5,11], target=10))