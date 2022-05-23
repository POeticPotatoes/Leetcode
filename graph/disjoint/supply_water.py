import heapq

class Solution:
    def minCostToSupplyWater(self, n, wells, pipes):

        pipes.sort(key = lambda x: x[2])
        costs = []
        for i,x in enumerate(wells):
            heapq.heappush(costs, [x, i])

        connected = 0
        tracked = [[-1, 1]] * n
        cost = 0
        
        def find(i):
            x = tracked[i]
            if x[0] < 0:
                return i
            n = find(x[0])
            x[0] = n
            x[1] = tracked[n][1]
            return n

        def buildWell(i, c):
            nonlocal cost, connected

            x = find(i)
            a = tracked[x]
            if a[0] != -1: return
            a[0] = -2
            connected += a[1]
            cost += c

        def buildPipe(a, b, c):
            nonlocal cost, connected

            a1 = find(a)
            b1 = find(b)
            a2 = tracked[a1]
            b2 = tracked[b1]

            if a2 == b2: return
            if a2[0] == -2:
                if b2[0] == -2:
                    return
                connected += b2[1]
            elif b2[0] == -2:
                connected += a2[1]

            if a2[1] > b2[1]:
                a2[1] += b2[1]
                b2[0] = a1
                b2[1] = a2[1]
                return
            b2[1] += a2[1]
            a2[0] = b1
            a2[1] = b2[1]

        return "Not Implemented"

    def helloWorld(self):
        return "winner winner"
