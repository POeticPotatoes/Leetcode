import unittest
from calc_equation import Solution

class TestCalcEquation(unittest.TestCase):
    solution = Solution()

    def test_works(self):
        self.assertEqual(self.solution.calcEquation(
            [["a","b"],["b","c"]], 
            [2.0,3.0], 
            [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]),
            [6.00000,0.50000,-1.00000,1.00000,-1.00000],
            "Works Normally")
    
    def test_works_disconnected(self):
        self.assertEqual(self.solution.calcEquation(
            [["a","b"],["b","c"],["bc","cd"]],
            [1.5,2.5,5.0], 
            [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]),
            [3.75000,0.40000,5.00000,0.20000],
            "Works on disconnected groups")
    
    def test_fails(self):
        self.assertEqual(self.solution.calcEquation(
            [["a","b"]],
            [0.5], 
            [["a","b"],["b","a"],["a","c"],["x","y"]]),
            [0.50000,2.00000,-1.00000,-1.00000],
            "Detects unused groups")
    
    def test_works_indirect(self):
        self.assertEqual(self.solution.calcEquation(
            [["a","b"],["e","f"],["b","e"]],
            [3.4,1.4,2.3],
            [["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]]),
            [0.29411764705882354, 10.947999999999999, 1.0, 1.0, -1, -1, 0.7142857142857143],
            "Works on indirectly linked nodes")
    
    def test_works_funny(self):
        self.assertEqual(self.solution.calcEquation(
            [["x1","x2"],["x2","x3"],["x1","x4"],["x2","x5"]],
            [3.0,0.5,3.4,5.6],
            [["x2","x4"],["x1","x5"],["x1","x3"],["x5","x5"],["x5","x1"],["x3","x4"],["x4","x3"],["x6","x6"],["x0","x0"]]),
            [1.13333,16.80000,1.50000,1.00000,0.05952,2.26667,0.44118,-1.00000,-1.00000],
            "Works on indirectly linked nodes")
    
    def test_hello_world(self):
        self.assertEqual(Solution().helloWorld(), "winner winner", "chicken dinner")
    
if __name__ == '__main__':
    print("started!")
    unittest.main()
