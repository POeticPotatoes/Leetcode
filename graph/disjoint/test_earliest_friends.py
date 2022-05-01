import unittest
from earliest_friends import Solution

class TestEarliestFriends(unittest.TestCase):
    solution = Solution()

    def test_works(self):
        self.assertEqual(self.solution.earliestAcq([[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], 4), 3, "Test works normally")
    
    def test_large(self):
        self.assertEqual(self.solution.earliestAcq([[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], 6), 20190301, "Test works on large numbers")
    
    def test_fails(self):
        self.assertEqual(self.solution.earliestAcq([[0,0,1]], 3), -1, "Test fails if not connected")
    
    def test_unsorted(self):
        self.assertEqual(self.solution.earliestAcq([[9,3,0],[0,2,1],[8,0,1],[1,3,2],[2,2,0],[3,3,1]], 4), 2, "Test works on unsorted times")
    
    def test_hello_world(self):
        self.assertEqual(Solution().helloWorld(), "winner winner", "chicken dinner")
    
if __name__ == '__main__':
    print("started!")
    unittest.main()
