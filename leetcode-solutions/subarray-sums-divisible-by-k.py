class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hmap = defaultdict(int)

        hmap[0]=1
        curr = 0
        count=0
        for num in nums:
            curr+=num
            count+=hmap[curr%k]
            hmap[curr%k]+=1
            
            
        return count
            