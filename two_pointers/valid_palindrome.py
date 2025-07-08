class Solution:
    def isPalindrome(self, s: str) -> bool:
        filter_s = ''.join(c.lower() for c in s if c.isalnum())
        start_ptr = 0
        end_ptr = len(filter_s) - 1

        while start_ptr <= end_ptr:
            if filter_s[start_ptr] != filter_s[end_ptr]:
                return False
            else:
                start_ptr += 1
                end_ptr -= 1

        return True


if __name__ == "__main__":
    test = Solution()
    print(test.isPalindrome(s = "No lemon, no melon"))