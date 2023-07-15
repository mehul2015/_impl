class Stack:

    def __init__(self) -> None:
        self.stack = []

    def append(self,num) -> None:
        self.stack.append(num)
    
    def pop(self):
        if self.isEmpty():
            return "There are no elements in the stack!"
        
        element_to_be_popped = self.stack[-1]
        self.stack = self.stack[0:len(self.stack) - 1]
        return element_to_be_popped        
    
    def peek(self):
       if self.isEmpty():
            return "There are no elements in the stack!"
       return self.stack[-1]

    
    def isEmpty(self) -> bool:
        return len(self.stack) == 0