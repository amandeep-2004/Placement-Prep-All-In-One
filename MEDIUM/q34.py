#Design a class that finds the kth largest element in a stream of integers.
import heapq

class KthLargest:
    def __init__(self, k):
        self.k = k
        self.heap = []

    def add(self, val):
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        if len(self.heap) < self.k:
            return None
        
        return self.heap[0]


k = int(input("Enter the value of K: "))
kth = KthLargest(k)

stream = [2, 5, 8, 4]

for x in stream:
    print(f"Add: {x} → {k}th largest: {kth.add(x)}")
