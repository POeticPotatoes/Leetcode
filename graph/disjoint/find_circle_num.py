# problem: problems/number-of-provinces
# Managed to solve the problem first try which is pretty pog
# Solution uses a disjoint list with updated indices, was efficient but slow.
# memory: O(n) to store disjoint set, complexity: O(nlog(n))

class Solution:
    sets = None

    def findCircleNum(self, isConnected):
        l = len(isConnected)
        if l == 1: return 1

        self.sets = list(range(l))
        count = 1
        for i in range(1, l):
            count += 1
            for x in range (i):
                if isConnected[i][x] == 0: continue
                num = self.getNum(x, i)
                if num != i: count -= 1
                
        return count

    def getNum(self, num, update):
        while self.sets[num] != num:
            n = self.sets[num]
            self.sets[num] = update
            num = n
        self.sets[num] = update
        return num

    def helloWorld(self):
        return "winner winner"
