import unittest
from valid_path import Solution, Solution2

class TestValidPath(unittest.TestCase):
    solution = Solution2()

    def test_works(self):
        self.assertEqual( self.solution.validPath(
            n = 3, 
            edges = [[0,1],[1,2],[2,0]], 
            source = 0, 
            destination = 2), 
            True, 
            "Works Normally");

    def test_fails(self):
        self.assertEqual( self.solution.validPath(
            n = 6, 
            edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], 
            source = 0, 
            destination = 5), 
            False, 
            "Fails if invalid");

    def test_hello_world(self):
        self.assertEqual(self.solution.helloWorld(), "winner winner", "chicken dinner")
    
if __name__ == '__main__':
    print("started!")
    unittest.main()
