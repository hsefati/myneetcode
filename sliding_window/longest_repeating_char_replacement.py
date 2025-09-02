class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_count = 0
        max_len = 0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            max_count = max(max_count, count[s[right]])

            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


if __name__ == "__main__":
    test = Solution()
    print(test.characterReplacement("AABABBA", 1))
    print(test.characterReplacement("XYYX", 2))
    print(test.characterReplacement("AAABABB", 1))
    print(test.characterReplacement("AAAB", 0))
