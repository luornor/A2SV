class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #[3,6,7,11] h=8
        #maxperhour could be the max number of piles
        # the answer will be in the range of (1-max(piles))
        def total_time(banana_piles,speed):
            time=0
            for num in banana_piles:
                time+=ceil(num/speed)
            return time
        
        time = 0
        l=1
        r=max(piles)
        while l<r:
            m=(l+r)//2
            time=total_time(piles,m)
            #we are looking for minimum
            if time<=h:
                r=m
            else:
                l=m+1

        return r

        