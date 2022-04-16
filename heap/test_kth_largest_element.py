import unittest
from kth_largest_element import Solution

class TestKthLargestElement(unittest.TestCase):

    def test_works(self):
        solution = Solution(3, [4,5,8,2])
        self.assertEqual(solution.add(3), 4, "")
        self.assertEqual(solution.add(5), 5, "")
        self.assertEqual(solution.add(10), 5, "")
        self.assertEqual(solution.add(9), 8, "")
        self.assertEqual(solution.add(4), 8, "")
    
    def test_works_again(self):
        solution = Solution(2, [0])
        self.assertEqual(solution.add(-1), -1, "")

    def test_works_on_small_arrays(self):
        solution = Solution(1, [])
        self.assertEqual(solution.add(3), 3, "Works on small arrays")

if __name__ == '__main__':
    print("started!")
    unittest.main()
