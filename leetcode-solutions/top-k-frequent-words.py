class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hmap = Counter(words)
        heap = [(-count,key) for key, count in hmap.items()]
        heapify(heap)

        res = []
        for _ in range(k):
            count,word = heappop(heap)
            res.append(word)
        
        # print(heap)
    
        return res



        