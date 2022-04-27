import unittest
from find_circle_num import Solution

class TestFindCircleNum(unittest.TestCase):
    solution = Solution()

    def test_works(self):
        self.assertEqual(self.solution.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]), 2, "Works normally")

    def test_disjointed(self):
        self.assertEqual(self.solution.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]), 3, "Works disjointed")
    
    def test_joined(self):
        self.assertEqual(self.solution.findCircleNum([[1,1,1],[1,1,1],[1,1,1]]), 1, "Works when all joined")
    
    def test_small(self):
        self.assertEqual(self.solution.findCircleNum([[1]]), 1, "Works on small sets")
    
    def test_hello_world(self):
        self.assertEqual(self.solution.helloWorld(), "winner winner", "chicken dinner")
    
if __name__ == '__main__':
    print("started!")
    unittest.main()
