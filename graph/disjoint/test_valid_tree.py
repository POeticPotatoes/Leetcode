import unittest
from valid_tree import Solution

class TestValidTree(unittest.TestCase):
    solution = Solution()

    def test_passes(self):
        self.assertEqual(self.solution.validTree(5, [[0,1],[0,2],[0,3],[1,4]]), True, "Works on valid trees")
    
    def test_fails(self):
        self.assertEqual(self.solution.validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]), False, "Fails on invalid trees")
    
    def test_circle(self):
        self.assertEqual(self.solution.validTree(5, [[0,1], [1,2], [2,3], [3,1]]), False, "Fails on disjointed trees")
    
    def test_circle(self):
        self.assertEqual(self.solution.validTree(5, [[0,1],[0,4],[1,4],[2,3]]), False, "Fails on grouped trees")
    
    def test_small(self):
        self.assertEqual(self.solution.validTree(1, []), True, "Works on small trees")
    
    def test_hello_world(self):
        self.assertEqual(Solution().helloWorld(), "winner winner", "chicken dinner")
    
if __name__ == '__main__':
    print("started!")
    unittest.main()
