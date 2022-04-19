import heapq

# problem: problems/kth-smallest-element-in-a-sorted-matrix
# Original solution: get all spots lesser or equal and rank them, ignoring areas beyond k
# Optimised to use max heap instead of min
# Solution suggested a counter for each row based on a minheap which would reduce memory required
# Additionally a binary search solution based on a theoretical midpoint with the closest number stored
class Solution:
    def kthSmallest(self, matrix, k):
        if len(matrix) == 1 or k == 1: return matrix[0][0]

        length = len(matrix) + 1
        heap = []
        for y in range(1, length):
            for x in range(1, length):
                if x * y > k: break
                heapq.heappush(heap, -matrix[y-1][x-1])
        while len(heap) > k: heapq.heappop(heap)
        return -heapq.heappop(heap)

    def helloWorld(self):
        return "winner winner"
