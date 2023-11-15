class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapify(heap)
        for i in range(k,len(nums)):
            heapq.heappush(heap,nums[i])
            heapq.heappop(heap)
        
        return heapq.heappop(heap)

        