import unittest
from smallest_with_swaps import Solution, Solution2

class TestSmallestWithSwaps(unittest.TestCase):
    solution = Solution2()

    def test_works(self):
        self.assertEqual(
                self.solution.smallestStringWithSwaps(
                    "dcab",
                    [[0,3],[1,2]]), 
                "bacd", 
                "Works normally")
    
    def test_works_overlapped(self):
        self.assertEqual(
                self.solution.smallestStringWithSwaps(
                    "dcab",
                    [[0,3],[1,2],[0,2]]),
                "abcd", 
                "Works when pairs overlap")

    def test_works_all(self):
        self.assertEqual(
                self.solution.smallestStringWithSwaps(
                    "cba",
                    [[0,1],[1,2]]),
                "abc", 
                "Works when all selected")

    def test_works_repeated(self):
        self.assertEqual(
                self.solution.smallestStringWithSwaps(
                    "qdwyt",
                    [[2,3],[3,2],[0,1],[4,0],[3,2]]),
                "dqwyt", 
                "Works when pairs repeat")
        
    def test_works_small(self):
        self.assertEqual(
                self.solution.smallestStringWithSwaps(
                    "cba",
                    []),
                "cba", 
                "Works without pairs")

    def test_hello_world(self):
        self.assertEqual(self.solution.helloWorld(), "winner winner", "chicken dinner")
    
if __name__ == '__main__':
    print("started!")
    unittest.main()
