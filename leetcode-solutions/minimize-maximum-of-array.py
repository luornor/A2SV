class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        def is_possible(nums,x):
            curr_sum = 0
            for i in range(len(nums)):
                curr_sum+=nums[i]
                if curr_sum > (i+1)*x:
                    return False
            
            return True

        l = 0
        r = max(nums)
        while l<r:
            m = (l+r)//2

            if is_possible(nums,m):
                r=m
            else:
                l=m+1

        return r

