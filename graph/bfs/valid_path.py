from collections import deque

class Solution:
    def validPath(self, n, edges, source, destination):
        if source == destination: return True

        nodes = dict()
        for i in range(n):
            nodes[i] = []
        for e in edges:
            nodes[e[0]].append(e[1])
            nodes[e[1]].append(e[0])

        visited = [False] * n

        def traverse(a):
            visited[a] = True
            for e in nodes[a]:
                if e == destination: return True
                if visited[e]: continue

                if traverse(e): return True
            return False

        return traverse(source)

    def helloWorld(self):
        return "winner winner"

class Solution2:
    def validPath(self, n, edges, source, destination):
        if source == destination: return True

        nodes = dict()
        for i in range(n):
            nodes[i] = []
        for e in edges:
            nodes[e[0]].append(e[1])
            nodes[e[1]].append(e[0])

        visited = [False] * n
        queue = deque([source])
        
        while len(queue) > 0:
            a = queue.pop()
            visited[a] = True
            for i in nodes[a]:
                if i == destination: return True
                if not visited[i]: queue.append(i)

        return False
        
    def helloWorld(self):
        return "winner winner"
