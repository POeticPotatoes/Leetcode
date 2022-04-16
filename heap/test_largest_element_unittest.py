import unittest
from largest_element import Solution

class TestKthLargestElement(unittest.TestCase):
    
    def test_hello_world(self):
        self.assertEqual(Solution().helloWorld(), "winner winner", "chicken dinner")
    
    def test_even_array(self):
        # Run tests
        self.assertEqual(Solution().findKthLargest([3,2,1,5,6,4], 2), 5, "Works on even arrays")
    
    def test_odd_array(self):
        # Run tests
        self.assertEqual(Solution().findKthLargest([3,2,1,2,4,5,5,6], 4), 4, "Works on odd arrays")

    def test_small_array(self):
        # Run tests
        self.assertEqual(Solution().findKthLargest([5], 1), 5, "Works on small arrays")

if __name__ == '__main__':
    print("started!")
    unittest.main()
