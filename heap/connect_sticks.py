import heapq

# problem: problems/minimum-cost-to-connect-sticks
# Answer was the same as my solution.
class Solution:
    def connectSticks(self, nums):
        if len(nums) == 1: return 0
        heapq.heapify(nums)
        sum = 0
        while len(nums) > 1:
            stick = heapq.heappop(nums) + heapq.heappop(nums)
            sum += stick
            heapq.heappush(nums, stick)
        return sum 

    def helloWorld(self):
        return "winner winner"
