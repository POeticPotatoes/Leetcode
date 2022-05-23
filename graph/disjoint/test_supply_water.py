import unittest
from supply_water import Solution

class TestSupplyWater(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        self.test(3, [1,2,2], [[1,2,1],[2,3,1]], 3, "Works normally")

    def test_2(self):
        self.test(2, [1,1], [[1,2,1],[1,2,2]], 2, "Works small")

    def test_3(self):
        self.test(4, [5,6,7,8], [[1,2,2], [3,4,1]], 3, "Works disjointed")

    def test(self, n, wells, pipes, val, desc):
        self.assertEqual(self.solution.minCostToSupplyWater(n, wells, pipes), val, desc)
    
    def test_hello_world(self):
        self.assertEqual(self.solution.helloWorld(), "winner winner", "chicken dinner")
    
if __name__ == '__main__':
    print("started!")
    unittest.main()
