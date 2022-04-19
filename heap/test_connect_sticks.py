import unittest
from connect_sticks import Solution

class TestConnectSticks(unittest.TestCase):
    solution = Solution()
    def test_odd(self):
        self.assertEqual(self.solution.connectSticks([2,4,3]), 14, "Works on odd arrays")
    
    def test_even(self):
        self.assertEqual(self.solution.connectSticks([1,8,3,5]), 30, "Works on even arrays")
    
    def test_small(self):
        self.assertEqual(self.solution.connectSticks([5]), 0, "Works on small arrays")
    
    def test_hello_world(self):
        self.assertEqual(Solution().helloWorld(), "winner winner", "chicken dinner")
    
if __name__ == '__main__':
    print("started!")
    unittest.main()
