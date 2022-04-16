import unittest
from k_weakest_rows import Solution

class TestKWeakestRows (unittest.TestCase):
    def test_works_odd(self):
        self.assertEqual(Solution().kWeakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], 3), [2,0,3], "Works on odd arrays")
    
    def test_works_even(self):
        self.assertEqual(Solution().kWeakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], 2), [0,2], "Works on even arrays")

    def test_hello_world(self):
        self.assertEqual(Solution().helloWorld(), "winner winner", "chicken dinner")
    
if __name__ == '__main__':
    print("started!")
    unittest.main()
