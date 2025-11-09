class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        target_hash_map, current_hash_map = {}, {}
        for char in t:
            target_hash_map[ord(char)] = target_hash_map.get(ord(char), 0) + 1

        left_index, right_index = 0, 0
        result = ""

        have, need = 0, len(target_hash_map)

        while right_index < len(s):
            if ord(s[right_index]) in target_hash_map:
                if (
                    current_hash_map.get(ord(s[right_index]), 0) + 1
                    == target_hash_map[ord(s[right_index])]
                ):
                    have += 1
                current_hash_map[ord(s[right_index])] = (
                    current_hash_map.get(ord(s[right_index]), 0) + 1
                )
            right_index += 1
            while have == need:
                if have == need:
                    if len(result) == 0 or len(result) > right_index - left_index:
                        result = s[left_index:right_index]

                if ord(s[left_index]) in target_hash_map:
                    current_hash_map[ord(s[left_index])] -= 1
                    if (
                        current_hash_map[ord(s[left_index])]
                        < target_hash_map[ord(s[left_index])]
                    ):
                        have -= 1
                left_index += 1

        return result


if __name__ == "__main__":
    test = Solution()
    print(test.minWindow(s="ADOBECODEBANC", t="ABC"))
    # print(test.minWindow(s="OUZODYXAZV", t="XYZ"))
    # print(test.minWindow(s="xyz", t="xyz"))
    # print(test.minWindow(s="x", t="xy"))
