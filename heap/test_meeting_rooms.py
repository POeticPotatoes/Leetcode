import unittest
from meeting_rooms import Solution

class TestMeetingRooms(unittest.TestCase):
    solution = Solution()
    def test_works(self):
        self.assertEqual(self.solution.minMeetingRooms([[0,30],[5,10],[15,20]]),2, "Works normally")

    def test_gives_1(self):
        self.assertEqual(self.solution.minMeetingRooms([[7,10],[2,4]]),1, "Gives 1 room")

    def test_works_small(self):
        self.assertEqual(self.solution.minMeetingRooms([[2,4]]),1, "Works on small arrays")

    def test_hello_world(self):
        self.assertEqual(self.solution.helloWorld(), "winner winner", "chicken dinner")
    
if __name__ == '__main__':
    print("started!")
    unittest.main()
