import heapq

# problem: problems/meeting-rooms-ii
# Original solution was nearly identical to solution 1 in leetcode, without a "Return if len(intervals) == 0" conditional
# Suggested solution was a combination of all start and end times into a sorted array and reading through to check for overlaps
class Solution:
    def minMeetingRooms(self, intervals):
        rooms = [0]
        intervals.sort()
        for i in intervals: 
            if rooms[0] <= i[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, i[1])

        return len(rooms) 

    def helloWorld(self):
        return "winner winner"
