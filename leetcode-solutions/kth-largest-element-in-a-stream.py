class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums=nums
        self.heap = self.nums.copy()
        heapify(self.heap)
        #get a heap of size k
        while len(self.heap)>k:
            heapq.heappop(self.heap)
            
       

    def add(self, val: int) -> int:
        #to prevent list index out of range
        #check if size is less thank k
        #only add numbers greater or equal to
        if len(self.heap)<self.k:
            heapq.heappush(self.heap,val)
        elif val >= self.heap[0]:
            heapq.heappush(self.heap,val) 
            heapq.heappop(self.heap)           
        
        # print(self.heap)
        return self.heap[0]
           

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)