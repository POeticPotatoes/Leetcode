from collections import deque
class Solution:
    def allPathsSourceTarget(self, graph):

        target = len(graph)-1
        ans = []

        stack = deque()
        stack.append([0])

        while True:
            i = stack.pop()

            for e in graph[i[-1]]:
                if e == target:
                    ans.append(i.copy() + [e])
                    continue
                a = i.copy() + [e]
                stack.append(a)

            if len(stack) == 0: break
                
        return ans

    def helloWorld(self):
        return "winner winner"
