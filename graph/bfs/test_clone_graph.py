import unittest
from clone_graph import Solution

class TestCloneGraph(unittest.TestCase):
    solution = Solution()
    
    def test_hello_world(self):
        self.assertEqual(self.solution.helloWorld(), "winner winner", "chicken dinner")
    
if __name__ == '__main__':
    print("started!")
    unittest.main()
