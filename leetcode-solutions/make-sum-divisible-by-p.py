class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        hmap = {0:-1}
        n = len(nums)

        ps = list(accumulate(nums))

        if ps[-1]%p==0:
            return 0

        count = n
        target = ps[-1]%p
        for i in range(n):
            curr = ps[i]%p

            hmap[curr]=i
            if (curr-target)%p in hmap:
                j = hmap[(curr-target)%p]
                count = min(count,i-j)
            


        return count if count!=n else -1
        


            

        