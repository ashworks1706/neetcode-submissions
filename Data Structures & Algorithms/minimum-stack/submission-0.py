class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        print(f"pushed {self.stack}")
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop(-1)
        print(f"popped {self.stack}")
        

    def top(self) -> int:
        print(f"topped {self.stack[-1]}")
        return self.stack[-1]
        

    def getMin(self) -> int:
        print(f"topped {min(self.stack)}")
        
        return min(self.stack)        
