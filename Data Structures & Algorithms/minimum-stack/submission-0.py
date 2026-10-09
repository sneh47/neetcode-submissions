class MinStack:

    def __init__(self):
        self.stack = []
        self.minval = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        #self.minval = min(self.minval, val)
        if not self.minval:
            self.minval.append(val)
        else:
            self.minval.append(min(val, self.minval[-1]))

    def pop(self) -> None:
        if not self.stack:
            return None
        self.minval.pop()
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        return self.minval[-1]
        
