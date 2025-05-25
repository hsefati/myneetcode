class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.insert(0, val)

    def pop(self) -> None:
        self.stack.pop(0)

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        return min(self.stack)

    def show(self):
        print(self.stack)


if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(1)
    minStack.show()
    minStack.push(2)
    minStack.show()
    minStack.push(0)
    minStack.show()
    print(minStack.getMin())
    minStack.pop()
    minStack.show()
    print(minStack.top())
    print(minStack.getMin())
