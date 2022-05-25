from collections import deque
class Solution:
    def cloneGraph(self, node):
        if node == None: return None

        nodes = {}
        def copyNode(o):
            n = Node()
            nodes[n.val] = n
            n.val = o.val
            for i in o.neighbors:
                if i.val in nodes:
                    n.neighbors.append(nodes[i.val])
                    continue
                n.neighbors.append(copyNode(i))
            return n

        return copyNode(node)

    def helloWorld(self):
        return "winner winner"

# Recursionless solution with BFS
class Solution2:
    def cloneGraph(self, node):
        if node == None: return None

        nodes = {}
        stack = deque()
        stack.append(node)
        count = 0

        while count < len(stack):
            for i in stack[count].neighbors:
                if i.val in nodes: continue
                nodes[i.val] = Node(i.val)
                stack.append(i)
                
            count += 1

        while len(stack) > 0:
            n = stack.pop()
            a = nodes[n.val]
            for i in n.neighbors:
                a.neighbors.append(nodes[i.val])

        return nodes[node.val]

    def helloWorld(self):
        return "winner winner"

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
