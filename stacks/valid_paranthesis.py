class Solution:
    def __init__(self):
        self.p_info = {
            "(": {"type": "opening", "match": ")"},
            ")": {"type": "closing", "match": "("},
            "{": {"type": "opening", "match": "}"},
            "}": {"type": "closing", "match": "{"},
            "[": {"type": "opening", "match": "]"},
            "]": {"type": "closing", "match": "["},
        }

    def isValid(self, s: str) -> bool:
        p_stack = []

        for item in s:
            if self.p_info[item]["type"] == "opening":
                p_stack.insert(0, item)
            else:  # then it is closing type
                if len(p_stack) > 0:
                    if self.p_info[item]["match"] == p_stack[0]:
                        if len(p_stack) > 0:
                            _ = p_stack.pop(0)
                    else:
                        p_stack.insert(0, item)
                else:
                    return False

        if len(p_stack) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    test = Solution()
    print(test.isValid(s="(])"))
