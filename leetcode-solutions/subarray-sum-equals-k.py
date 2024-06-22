class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        hmap = defaultdict(int)

        hmap[0]=1
        curr = 0
        count=0
        for num in nums:
            curr+=num
            if curr-k in hmap:
                count+=hmap[curr-k]

            if curr in hmap:
                hmap[curr] += 1
            else:
                hmap[curr] = 1
            
            
        return count