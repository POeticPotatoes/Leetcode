import heapq

# problem: problems/find-median-from-data-stream
# My solution was the same as answer #2
# I had a lot of trouble in forgetting to invert the max heap (clown moment)
# The answer has an insane binary search strategy that I should definitely go back to read again.
class Solution:
    def furthestBuilding(self, heights, bricks, ladders):
        if len(heights) == 1: return 0
        bricked = []
        for i in range(1, len(heights)):
            if heights[i] <= heights[i-1]: continue
            diff = heights[i] - heights[i-1]
            if diff <= bricks:
                bricks -= diff 
                heapq.heappush(bricked, -diff)
                continue
            if len(bricked) == 0 or diff >= -bricked[0]:
                if ladders == 0: return i-1
                ladders -= 1
                continue
            while bricks <= diff:
                if ladders == 0: return i-1
                ladders -= 1
                bricks += -heapq.heappop(bricked)
            bricks -= diff
            heapq.heappush(bricked, -diff)
        return len(heights) -1

    def helloWorld(self):
        return "winner winner"
