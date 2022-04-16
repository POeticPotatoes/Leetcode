import unittest
from most_frequent import Solution

class TestMostFrequent(unittest.TestCase):
    def test_even_array(self):
        self.assertEqual(Solution().topKFrequent([1,1,2,2,3,4], 2), [1,2], "Works on even arrays")

    def test_odd_array(self):
        self.assertEqual(Solution().topKFrequent([4,6,7,7,8,3,3,3,2,4,1], 3), [3, 4, 7], "Works on odd arrays")

    def test_small_array(self):
        self.assertEqual(Solution().topKFrequent([6], 1), [6], "Works on small arrays")

    def test_hello_world(self):
        self.assertEqual(Solution().helloWorld(), "winner winner", "chicken dinner")
    
if __name__ == '__main__':
    print("started!")
    unittest.main()
