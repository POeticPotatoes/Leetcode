class MedianFinder:
    values = []
    median = 0

    def addNum(self, num):
        print("AddNum", num)
        if (len(self.values) != 0 and self.values[self.median] > num):
            self.values.insert(0, num)
            self.median += 1
            return
        self.values.append(num)
        return "Not Implemented"

    def findMedian(self):
        print("FindMedian", self.values)
        median = len(self.values)//2
        if (median == self.median):
            return self.values[median]
        return "Not Implemented"
    
    def helloWorld(self):
        return "winner winner"
