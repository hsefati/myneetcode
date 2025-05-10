class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_arr = list(s)
        t_arr = list(t)
        for letter in s_arr:
            if letter in t_arr:
                t_arr.remove(letter)
            else:
                return False
        if len(t_arr) > 0:
            return False
        return True



if __name__ == "__main__":
    test = Solution()
    print(test.isAnagram(s = "jar", t = "jam"))
    print(ord('s'))