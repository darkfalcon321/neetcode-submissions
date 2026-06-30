class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.min = float('inf')

    def push(self, value: int) -> None:
        self.stack.append(value)
        
        if not self.minStack:
            self.minStack.append(value)
            self.min = value
        
        else:
            self.min = min(self.minStack[-1], value)
            self.minStack.append(self.min)
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minStack.pop()
            if self.minStack:
                self.min = self.minStack[-1]
            else:
                self.min = float('inf')
                                        
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return 0

    def getMin(self) -> int:
        if self.stack:
            return self.minStack[-1]
        else:
            return 0


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()