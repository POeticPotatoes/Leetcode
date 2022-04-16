import heapq

class Solution:
    def __init__(self, k, nums): 
        self.heap = nums
        self.k = k
        if len(self.heap) == 0:
            return
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, num):
        if len(self.heap) >= self.k and self.heap[0] >= num:
            return self.heap[0]
        heapq.heappush(self.heap, num)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
