from heapq import *

"""
Using two heaps to find median: large heap and small heap. largeHeap contains the 
larger half part of the input data, and smallHeap contains smaller half part value.

Put the first 2 numbers in largeHeap, then pop the smaller one and push it into smallHeap. 
The same for the following numbers, adding them to the largeHeap first and make sure 
the balance between those 2 heaps. That is, the alrgeHeap at most contain 1 more node 
than the smallHeap. In this way, we can get the median number from roots of the heaps. 

If the largeHeap contains 1 more node, then its root would be the median, which occurs
when the number of input lines is odd. On the other hand, if the two heaps contain the 
same amount of nodes, which means we have even input lines, then we can get the median 
by computing the average value of the two roots.

time complexity of adding a new number is O(logn) and getting median is O(1)
"""

class GetMedianByHeap:
    def __init__(self):
        self.largeHeap = []
        self.smallHeap = []
        self.totalAMT = 0
    
    """add numbers to heaps, making sure the balance between them, 
       since heapq is a min heap, which always pops the min value of the PriorityQueue, 
       using negation in the smallHeap, so that when it pops the value, with the negation, 
       we can directly get the max value from the smaller half part.
    """
    def add(self,num):
        heappush(self.largeHeap,num)
        heappush(self.smallHeap,-heappop(self.largeHeap))
        if len(self.largeHeap)<len(self.smallHeap):
            heappush(self.largeHeap,-heappop(self.smallHeap))
        self.totalAMT+=num
    
    #median of the current data
    def getMedian(self):
        if len(self.largeHeap)>len(self.smallHeap):
            return self.largeHeap[0]
        return int(round((self.largeHeap[0]-self.smallHeap[0])/2.0))
    
    #total contribution amount 
    def getTotalAMT(self):
        return self.totalAMT
    
    #total transaction numbers
    def getTotalTrans(self):
        return len(self.largeHeap)+len(self.smallHeap)
