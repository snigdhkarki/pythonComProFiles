class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

stack = Stack()
# stack.push(10)
# stack.push(20)
# print("Stack peek:", stack.peek())
# print("Stack pop:", stack.pop())
# print("Stack after pop:", stack.stack)
