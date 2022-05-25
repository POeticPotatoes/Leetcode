import heapq

# problem: problems/smallest-string-with-swaps/
# This problem was pretty hard, found a solution with disjoint sets leading up to a heap of characters
# Attempted to further optimise it by simply storing the values as a list and sorting them once but it actually resulted in a longer time since there were more writes to array.

class Solution:
    groups: list

    def smallestStringWithSwaps(self, s, pairs):
        if len(pairs) == 0:
            return s
        self.groups = list(c for c in s)
        
        for p in pairs:
            self.union(p[0], p[1])

        ans = ""
        for i in range(len(s)):
            a = self.get(i)
            v = self.groups[a]

            val = None
            if type(v) == str: val = v
            else: val = heapq.heappop(v)
            ans += val

        return ans

    def union(self, a, b):
        x = self.get(a)
        y = self.get(b)
        if x == y: return
        vx = self.groups[x]
        vy = self.groups[y]
        if type(vx) == list:
            if type(vy) != list:
                heapq.heappush(vx, vy)
                self.groups[y] = x
                return
            if len(vx) > len(vy):
               for i in vy:
                   heapq.heappush(vx, i)
               self.groups[y] = x
               return
            for i in vx:
               heapq.heappush(vy, i)
            self.groups[x] = y
            return
        if type(vy) == list:
            heapq.heappush(vy, vx)
            self.groups[x] = y
            return
        if vx < vy:
            self.groups[x] = [vx, vy]
            self.groups[y] = x
            return
        self.groups[y] = [vy, vx]
        self.groups[x] = y
        return;

    def get(self, num):
        v = self.groups[num]
        if type(v) == int:
            return self.get(v)
        return num

    def helloWorld(self):
        return "winner winner"

class Solution2:
    groups: list

    def smallestStringWithSwaps(self, s, pairs):
        if len(pairs) == 0:
            return s
        self.groups = list(c for c in s)
        
        for p in pairs:
            self.union(p[0], p[1])

        ans = ""
        count = [0] * len(s)
        for i in range(len(s)):
            x = self.get(i)
            v = self.groups[x]
            if type(v) == str:
                ans += v
                continue
            if count[x] == 0:
                v.sort()
            ans += v[count[x]]
            count[x] += 1

        return ans

    def union(self, a, b):
        x = self.get(a)
        y = self.get(b)
        if x == y: return
        vx = self.groups[x]
        vy = self.groups[y]
        if type(vx) == list:
            if type(vy) == list:
                self.groups[x] = vx + vy
                self.groups[y] = x
                return
            vx.append(vy)
            self.groups[y] = x
            return
        if type(vy) == list:
            vy.append(vx)
            self.groups[x] = y
            return
        self.groups[x] = [vx, vy]
        self.groups[y] = x

    def get(self, num):
        v = self.groups[num]
        if type(v) == int:
            return self.get(v)
        return num

    def helloWorld(self):
        return "winner winner"
