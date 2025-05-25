from typing import List


class Solution:
    def __init__(self):
        self.stack = []
        self.operators = ["+", "-", "*", "/"]

    def evalRPN(self, tokens: List[str]) -> int:
        for item in tokens:
            if item not in self.operators:
                self.stack.append(int(item))
            else:
                b = self.stack.pop()
                a = self.stack.pop()
                if item == "+":
                    self.stack.append(a + b)
                elif item == "-":
                    self.stack.append(a - b)
                elif item == "*":
                    self.stack.append(a * b)
                elif item == "/":
                    self.stack.append(int(a / b))
        return self.stack[0]


if __name__ == "__main__":
    test = Solution()
    print(test.evalRPN(tokens=["4", "13", "5", "/", "+"]))
