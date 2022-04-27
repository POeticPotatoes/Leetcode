import unittest
from median_finder import MedianFinder

class TestMedianFinder(unittest.TestCase):
    def test_works(self):
        self.runSequence([[1], [2], [], [3], []], [1.5,2.0])
 
    def runSequence(self, sequence, results):
        finder = MedianFinder()
        count = 0;
        for x in sequence:
            if len(x) == 0:
                print("AssertEqual", results[count])
                self.assertEqual(finder.findMedian(), results[count])
                count += 1
                continue
            finder.addNum(x[0])
    
    def test_hello_world(self):
        self.assertEqual(MedianFinder().helloWorld(), "winner winner", "chicken dinner")
    
if __name__ == '__main__':
    print("started!")
    unittest.main()
