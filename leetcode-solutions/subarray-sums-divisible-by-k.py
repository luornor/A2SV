class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        window = defaultdict(int)
        window[0] =1
        currsum = 0
        r = 0
        count = 0
        while r<len(nums):
            currsum+=nums[r]
            remainder = currsum% k
            count += window[remainder]
            if remainder in window:
                # currsum-=nums[l]
                window[remainder]+=1
            else:
                window[remainder]=1
            r+=1

        return count
            

