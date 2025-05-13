from typing import List


class Solution:

    def encode(self, strs):
        """Encodes a list of strings to a single string."""
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s):
        """Decodes a single string back to a list of strings."""
        res, i = [], 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            i = j + 1 + length
            res.append(s[j + 1 : i])
        return res


if __name__ == "__main__":
    test = Solution()
    encoded = test.encode(["neet", "code", "love", "you"])
    print(encoded)
    print(test.decode(encoded))
