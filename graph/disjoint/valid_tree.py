# Problem: problems/graph-valid-tree
# I was very frustrated because I felt like my solution wasn't the best, but it's the third solution in Leetcode
# At least it's really good in speed and memory

class Solution:

    x = None

    def validTree(self, n, edges):
        if n == 1: return True
        if len(edges) != n-1: return False

        self.x = list(range(n))

        for e in edges:
            self.corrupt(e[0], e[1])
            self.corrupt(e[1], e[1])
        num = edges[len(edges)-1][1]

        for e in self.x:
            if self.find(e) != num: return False
        return True

    def corrupt(self, num, u):
        while self.x[num] != u:
            n = self.x[num]
            self.x[num] = u
            num = n
    
    def find(self, num):
        while self.x[num] != num:
            n = self.x[num]
            self.x[num] = self.x[n]
            num = n
        return self.x[num]

    def helloWorld(self):
        return "winner winner"
