import heapq

class Solution:
    def findKthLargest(self, nums, k):
        # nums: array, k: int
        heap = [-x for x in nums] 
        heapq.heapify(heap)
        for i in range(k-1):
            heapq.heappop(heap)
        return -1 * heapq.heappop(heap)


    def helloWorld(self):
        return "winner winner"
