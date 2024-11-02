from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return None  

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return None

    def is_empty(self):
        return len(self.queue) == 0

queue = Queue()
# queue.enqueue(10)
# queue.enqueue(20)
# print("Queue peek:", queue.peek()) 
# print("Queue dequeue:", queue.dequeue()) 
# print("Queue after dequeue:", list(queue.queue))
