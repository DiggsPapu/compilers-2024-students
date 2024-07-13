class Stack():
    def __init__(self):
        self.stack = []
    def peek(self):
        return self.stack[len(self.stack)-1]
    def pop(self):
        return self.stack.pop()
    def push(self, newElement):
        self.stack.append(newElement)