# Problem: problems/k-closest-points-to-origin
# Decided to implement a binary search to solve instead of heap
# Encountered issues due to differences in how python versions handled int and floats
# Worth noting that manually converting a value to a float might be a good idea
# Solution beat almost 100% of solutions in memory :D
# Answer suggests using quickselect for constant memory
class Solution:
    def kClosest(self, points, k):
        if k == len(points): return points
        start = 0
        end = 0
        for i in points:
            end = max(abs(i[0]), abs(i[1]), end)
        end += 1.0 # convert to float
        middle = (end * k)/len(points)
        count = []
        while True:
            square = middle * middle * 2
            for i in points:
                if i[0] * i[0] + i[1] * i[1] <= square: count.append(i)
            if len(count) == k: break
            if len(count) < k:
                start = middle
            else: end = middle
            middle = (start+end)/2
            count = []
        return count 

    def helloWorld(self):
        return "winner winner"
