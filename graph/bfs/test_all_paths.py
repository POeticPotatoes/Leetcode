import unittest
from all_paths import Solution

class TestAllPaths(unittest.TestCase):
    solution = Solution()

    def test_works(self):
        self.assertEqual(self.solution.allPathsSourceTarget(
            [[1,2],[3],[3],[]]), 
            [[0,1,3],[0,2,3]], 
            "Works Normally")
    
    def test_more(self):
        self.assertEqual(self.solution.allPathsSourceTarget(
            [[4,3,1],[3,2,4],[3],[4],[]]), 
            [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]], 
            "Works well")
    
    def test_hello_world(self):
        self.assertEqual(self.solution.helloWorld(), "winner winner", "chicken dinner")
    
if __name__ == '__main__':
    print("started!")
    unittest.main()
