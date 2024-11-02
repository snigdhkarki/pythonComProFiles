import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        heapq.heappush(self.heap, value)

    def find_min(self):
        if self.heap:
            return self.heap[0]
        return None

    def extract_min(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        heapq.heappush(self.heap, -value)

    def find_max(self):
        if self.heap:
            return -self.heap[0]
        return None

    def extract_max(self):
        if self.heap:
            return -heapq.heappop(self.heap)
        return None

# min_heap = MinHeap()
# min_heap.insert(10)
# min_heap.insert(5)
# min_heap.insert(20)
# print("MinHeap find_min:", min_heap.find_min()) 
# print("MinHeap extract_min:", min_heap.extract_min())
# print("MinHeap extract_min:", min_heap.extract_min())
# print("MinHeap after extract_min:", min_heap.heap)

# max_heap = MaxHeap()
# max_heap.insert(10)
# max_heap.insert(5)
# max_heap.insert(20)
# print("MaxHeap find_max:", max_heap.find_max()) 
# print("MaxHeap extract_max:", max_heap.extract_max())
# print("MaxHeap after extract_max:", [-x for x in max_heap.heap])
