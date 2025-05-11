from typing import List
from collections import Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_anagrams = []
        checked_strs = []
        for i in range(len(strs)):
            if strs[i] not in checked_strs:
                anagrams = [strs[i]]
                for j in range(i + 1, len(strs)):
                    if Counter(strs[i]) == Counter(strs[j]):
                        anagrams.append(strs[j])
                        checked_strs.append(strs[j])
                        checked_strs.append(strs[i])
                if anagrams:
                    list_anagrams.append(anagrams)

        return list_anagrams


if __name__ == "__main__":
    test = Solution()
    print(test.groupAnagrams(strs=["", ""]))
