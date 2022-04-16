import unittest
from k_weakest_rows import Solution, Solution2

class TestKWeakestRows (unittest.TestCase):
    solution = Solution2()
    def test_works_odd(self):
        self.assertEqual(self.solution.kWeakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], 3), [2,0,3], "Works on odd arrays")
    
    def test_works_even(self):
        self.assertEqual(self.solution.kWeakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], 2), [2,0], "Works on even arrays")

    def test_works_max(self):
        self.assertEqual(self.solution.kWeakestRows([[1,1,1,1,1,1],[1,1,1,1,1,1],[1,1,1,1,1,1]], 1), [0],"Works on maxed arrays")

    def test_hello_world(self):
        self.assertEqual(self.solution.helloWorld(), "winner winner", "chicken dinner")
    
if __name__ == '__main__':
    print("started!")
    unittest.main()
