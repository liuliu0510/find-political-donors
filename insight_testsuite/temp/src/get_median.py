from heapq import *

class GetMedianByHeap:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        self.totalAMT = 0
    
    def add(self,num):
        heappush(self.maxHeap,num)
        heappush(self.minHeap,-heappop(self.maxHeap))
        if len(self.maxHeap)<len(self.minHeap):
            heappush(self.maxHeap,-heappop(self.minHeap))
        self.totalAMT+=num
    
    def getMedian(self):
        if len(self.maxHeap)>len(self.minHeap):
            return self.maxHeap[0]
        return int(round((self.maxHeap[0]-self.minHeap[0])/2.0))
    
    def getTotalAMT(self):
        return self.totalAMT
    
    def getTotalTrans(self):
        return len(self.maxHeap)+len(self.minHeap)
