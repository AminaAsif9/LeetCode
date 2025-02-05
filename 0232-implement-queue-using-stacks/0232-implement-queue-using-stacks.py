class MyQueue:
    def __init__(self):
        self.stackin=[]
        self.stackout=[]

    def push(self, x: int) -> None:
        self.stackin.append(x) #add new val in 1st stack

    def pop(self) -> int:
        if not self.stackout:
            while (self.stackin):
                self.stackout.append(self.stackin.pop()) #reversing 1st stack and storing reversed in 2nd stack
        return self.stackout.pop()

    def peek(self) -> int: #peek = return without removing
        if not self.stackout:
            while (self.stackin):
                self.stackout.append(self.stackin.pop())
        return self.stackout[-1]

    def empty(self) -> bool:
        return not self.stackin and not self.stackout


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()