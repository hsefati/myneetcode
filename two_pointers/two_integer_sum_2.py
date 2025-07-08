
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start_ptr = 0
        end_ptr = len(numbers) - 1

        while start_ptr < end_ptr:
            if numbers[start_ptr] + numbers[end_ptr] == target:
                return [start_ptr + 1, end_ptr + 1]
            elif numbers[start_ptr] + numbers[end_ptr] < target:
                start_ptr += 1
            else:
                end_ptr -= 1
        return []

if __name__ == "__main__":
    test = Solution()
    print(test.twoSum(numbers = [1,2,3,4], target = 3))