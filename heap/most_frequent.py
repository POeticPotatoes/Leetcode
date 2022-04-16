import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        if k == len(nums):
            return nums

        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)