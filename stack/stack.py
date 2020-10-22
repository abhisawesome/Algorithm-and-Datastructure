class Stack:
    # Constructor to initialize stack
    def __init__(self,stack):
        self.stack = stack

    # Push operation
    def push(self,value):
        self.stack.append(value)
    
    # Pop operation
    def pop(self):
        self.stack.pop()
    
    # get current stack
    def returnStack(self):
        return self.stack

x= Stack([1,2,3,4])
x.push(44)
print('stack After Push operation',x.returnStack())
x.pop()
print('stack After Pop operation',x.returnStack())
