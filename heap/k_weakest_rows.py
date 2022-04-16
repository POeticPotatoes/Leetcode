import heapq

# Problem: problems/the-k-weakest-rows-in-a-matrix 
# My solution was nearly identical to solution 2 in the answers :)
# I didn't know about python's enumerate() method so I'll use it next time
# Solution also recommended binary search instead of linear search to determine strength
class Solution:
    def kWeakestRows(self, nums, k):
        strengths = [0] * (1+len(nums[0]))
        for x in range(len(nums)): 
            row = nums[x]
            count = 0
            for i in row:
                if i == 0:
                    break
                count+=1
            if strengths[count] == 0:
                strengths[count] = []
            strengths[count].append(x)
        ans = []
        for row in strengths:
            if row == 0:
                continue
            for i in row:
                if len(ans) == k:
                    break
                ans.append(i)
            if len(ans) == k:
                break
        return ans

    def helloWorld(self):
        return "winner winner"

# Second solution that doesn't involve any counting, written after referring to solution
class Solution2:
    def kWeakestRows(self, nums, k):
        ans = []
        total = len(nums[0])
        for i in range(total + 1):
            for r, row in enumerate(nums):
                if len(ans) == k: break
                if i != total and row[i] == 1: continue
                if i > 0 and row[i-1] == 0: continue
                ans.append(r)
            if len(ans) == k: break
        return ans

    def helloWorld(self):
        return "winner winner"

