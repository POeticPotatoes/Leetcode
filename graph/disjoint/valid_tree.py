# Problem: problems/graph-valid-tree
# I was very frustrated because I felt like my solution wasn't the best, but it's the third solution in Leetcode
# Finally figured out why! now I'm just tracking the count so there's no final iteration through the array. :D

class Solution:

    x = None

    def validTree(self, n, edges):
        if n == 1: return True
        if len(edges) != n-1: return False

        self.x = list(range(n))
        count = n

        for e in edges:
            a = self.corrupt(e[1], e[1])
            b = self.corrupt(e[0], e[1])
            if b != e[1]: count -= 1

        return count == 1

    def corrupt(self, num, u):
        if self.x[num] != num:
            n = self.x[num]
            if n == u: return u
            self.x[num] = u
            return self.corrupt(n, u)
        n = self.x[num]
        if n!= u: self.x[num] = u
        return n
    
    def helloWorld(self):
        return "winner winner"
