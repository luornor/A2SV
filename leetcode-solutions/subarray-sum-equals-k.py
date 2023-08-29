class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currsum = 0
        count = 0
        prefixsum = {0:1}
        for num in nums:
            currsum += num
            if currsum - k in prefixsum:
                count += prefixsum[currsum - k]
            prefixsum[currsum] = prefixsum.get(currsum, 0) + 1

        return count