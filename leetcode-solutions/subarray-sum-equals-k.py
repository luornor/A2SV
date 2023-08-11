def subarraySum(nums,k):
        currsum = 0
        count = 0
        prefixsum = {0:1}
        for num in nums:
            currsum += num
            if currsum - k in prefixsum:
                count += prefixsum[currsum - k]
            if currsum in prefixsum:
                prefixsum[currsum] += 1
            else:
                prefixsum[currsum] = 1

        return count