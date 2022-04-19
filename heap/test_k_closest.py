import unittest
from k_closest import Solution

class TestKClosest(unittest.TestCase):
    solution = Solution()
    def test_works(self):
        self.assertEqual(self.solution.kClosest([[3,3],[5,-1],[-2,4]], 2),[[3,3],[-2,4]], "Works Normally")
    
    def test_works_again(self):
        self.assertEqual(self.solution.kClosest([[-5,4],[-6,-5],[4,6]], 2), [[-5,4],[4,6]], "Works Normally")
    
    def test_works_again_again(self):
        self.assertEqual(self.solution.kClosest([[3,3],[5,-1],[-2,4]], 2), [[3,3], [-2,4]], "Works Normally")
    
    def test_small_array(self):
        self.assertEqual(self.solution.kClosest([[3,3]], 1),[[3,3]], "Works on small arrays")
    
    def test_hello_world(self):
        self.assertEqual(Solution().helloWorld(), "winner winner", "chicken dinner")
    
if __name__ == '__main__':
    print("started!")
    unittest.main()
