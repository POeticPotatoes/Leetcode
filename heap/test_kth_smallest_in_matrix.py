import unittest
from kth_smallest_in_matrix import Solution

class TestKthSmallestInMatrix(unittest.TestCase):
    solution = Solution()

    def test_works_normally(self):
        self.assertEqual(self.solution.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8), 13, "Works normally")

    def test_small_matrix(self):
        self.assertEqual(self.solution.kthSmallest([[-5]], 1), -5, "Works on small arrays")

    def test_messy_matrix(self):
        self.assertEqual(self.solution.kthSmallest([[1,3],[2,4]], 2), 2, "Works on messy arrays")

    def test_messier_matrix(self):
        self.assertEqual(self.solution.kthSmallest([[1,3,5],[6,7,12],[11,14,14]], 3), 5, "Works on really messy arrays")

    def test_hello_world(self):
        self.assertEqual(self.solution.helloWorld(), "winner winner", "chicken dinner")
    
if __name__ == '__main__':
    print("started!")
    unittest.main()
