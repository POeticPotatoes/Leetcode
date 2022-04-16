import unittest
from last_stone_weight import Solution

class TestLastStoneWeight(unittest.TestCase):
    def test_works(self):
        self.assertEqual(Solution().lastStoneWeight([2,7,4,1,8,1]), 1, "Works normally")

    def test_small_arrays(self):
        self.assertEqual(Solution().lastStoneWeight([1]), 1, "Works on small arrays")

    def test_hello_world(self):
        self.assertEqual(Solution().helloWorld(), "winner winner", "chicken dinner")
    
if __name__ == '__main__':
    print("started!")
    unittest.main()
