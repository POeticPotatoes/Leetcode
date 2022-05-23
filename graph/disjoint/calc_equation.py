class Solution:
    def calcEquation(self, equations, vals, queries):
        values = {}

        def find(v):
            a = values.get(v)
            if a is None or a[0] == v: return a
            x = find(a[0])
            n = (x[0], x[1] * a[1])
            values[v] = n
            return n
        
        def union(a, b, r):
            a1 = find(a)
            b1 = find(b)
            print(a1, b1)

            if a1 is None: a1 = (a, 1)
            if b1 is None: 
                b1 = (b, 1)
                values[b1[0]] = b1
            values[a1[0]] = (b1[0], r * b1[1] / a1[1])

        for i, x in enumerate(equations):
            union(x[0], x[1], vals[i])
            print(values)

        ans = [-1]*len(queries)
        for i, x in enumerate(queries):
            a = find(x[0])
            print(values)
            b = find(x[1])
            print(values)
            if a is None or b is None or a[0] != b[0]: continue

            ans[i] = a[1]/b[1]

        return ans

    def helloWorld(self):
        return "winner winner"
