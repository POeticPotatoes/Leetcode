import unittest
from furthest_building import Solution

class TestFurthestBuilding(unittest.TestCase):
    solution = Solution()
    def test_even(self):
        self.assertEqual(self.solution.furthestBuilding([4,2,7,6,9,14,12], 5, 1), 4, "Works on even arrays")

    def test_odd(self):
        self.assertEqual(self.solution.furthestBuilding([4,12,2,7,3,18,20,3,19], 10, 2), 7, "Works on odd arrays")

    def test_reachend(self):
        self.assertEqual(self.solution.furthestBuilding([14,3,19,3], 17, 0), 3, "Finishes array")

    def test_small(self):
        self.assertEqual(self.solution.furthestBuilding([3], 17, 3), 0, "Works on small arrays")

    def test_ladderspam(self):
        self.assertEqual(self.solution.furthestBuilding([1,13,1,1,13,5,11,11], 10, 8), 7, "Works on ladderspam")

    def test_brickspam(self):
        self.assertEqual(self.solution.furthestBuilding([1,13,1,1,13,5,11,11], 10, 8), 7, "Works on ladderspam")

    def test_hello_world(self):
        self.assertEqual(Solution().helloWorld(), "winner winner", "chicken dinner")
    
if __name__ == '__main__':
    print("started!")
    unittest.main()
