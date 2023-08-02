def maximumSubarraySum(nums,k):
        currsum = 0
        maxsum = 0
        l = 0
        window = set()
        for r in range(len(nums)):
            while l < r and (nums[r] in window or len(window) >= k):
                currsum -= nums[l]
                window.remove(nums[l])
                l += 1
            currsum += nums[r]
            window.add(nums[r])
            if len(window) == k:
                maxsum = max(maxsum, currsum)
        return maxsum