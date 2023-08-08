def countCompleteSubarrays(nums):
        window = {}
        distinct_nums = set(nums)
        n = len(nums)
        l,r = 0,0
        count=0
        while r<n:
            window[nums[r]] = 1+ window.get(nums[r],0)

            while len(distinct_nums)==len(window):
                count+=n-r
                window[nums[l]]-=1
                if window[nums[l]]==0:
                    del window[nums[l]]
                l+=1
            r+=1

        return count