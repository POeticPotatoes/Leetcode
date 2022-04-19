import heapq

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
