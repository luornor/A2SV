class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = [-num for num in stones]
        heapify(heap)
        while len(heap)>1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            if x==y:
                continue
            if x>=y:
                y=y-x
                heapq.heappush(heap,y)

        if heap:
            return abs(heapq.heappop(heap))
        else:
            return 0

                


        