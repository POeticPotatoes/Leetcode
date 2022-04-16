import heapq

class Solution:
    def lastStoneWeight(self, nums):
        heap = [-x for x in nums]
        heapq.heapify(heap)
        while len(heap) > 1:
            count = heapq.heappop(heap) - heapq.heappop(heap)
            heapq.heappush(heap, count)
        return -1 * heapq.heappop(heap)

    def helloWorld(self):
        return "winner winner"
