fro heapq

class GetMedianByHeap:
    def _init_(self):
        self.maxHeap=[]
        self.minHeap=[]
        self.totalAMT=0
    
    def add(self,num):
        heappush(self.maxHeap,num)
        heappush(self.minHeap,-heappop(self.maxHeap))
        if len(self.maxHeap)<len(self.minHeap):
            heappush()