import heapq

# Problem: problems/the-earliest-moment-when-everyone-become-friends
# Solution was fast and efficient, with optimisations to prevent unnecessary writes to my array.
# Additionally switched to recursion in my corrupt method
# I opted to use heap instead of sorting in anticipation that not all arrays had to be fully sorted.
class Solution:
    nums = None

    def earliestAcq(self, logs, n):
        heapq.heapify(logs)
        self.nums = list(range(n))

        count = n
        while len(logs) > 0:
            x = heapq.heappop(logs)
            a = self.corrupt(x[1], x[1])
            b = self.corrupt(x[2], x[1])
            if b != x[1]:
                count -= 1
            if count == 1:
                return x[0]
        return -1

    def corrupt(self, n, u):
        if self.nums[n] != n:
            a = self.nums[n]
            if a == u: return u
            self.nums[n] = u
            return self.corrupt(a, u)
        a = self.nums[n]
        if a != u: self.nums[n] = u
        return a
    
    def helloWorld(self):
        return "winner winner"
