class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.len = 0

    def push(self, x: int) -> None:
        if not self.len or self.stack[-1][1]>x:
            self.stack.append([x, x])
        else:
            self.stack.append([x, self.stack[-1][1]])
        self.len+=1


    def pop(self) -> None:
        e = self.stack.pop()
        self.len-=1
        return e[1]
    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()