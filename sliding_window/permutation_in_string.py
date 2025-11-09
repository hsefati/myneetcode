class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = right = 0

        while left < len(s2) and right < len(s2):
            if s2[right] in s1:
                s1 = s1.replace(s2[right], "", 1)
                right += 1
            else:
                if right > left:
                    s1 = s1 + s2[left]
                    left += 1
                else:
                    right += 1
                    left += 1
            if s1 == "":
                return True
        return False


if __name__ == "__main__":
    test = Solution()
    # print(test.checkInclusion(s1="adc", s2="dcda"))
    # print(test.checkInclusion(s1="abc", s2="lecabee"))
    # print(test.checkInclusion(s1="abc", s2="lecaabee"))
    print(test.checkInclusion(s1="abc", s2="leccabee"))
