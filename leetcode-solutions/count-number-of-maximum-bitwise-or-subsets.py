class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = nums[0]

        for i in range(1,len(nums)):
            max_or = max_or | nums[i]
            
        res = [[]]
        for num in nums:
            res+=[arr+ [num] for arr in res]

        count = 0
        for arr in res:
            if arr:
                check = arr[0]
                for i in range(1,len(arr)):
                    check = check | arr[i]

                if check==max_or:
                    count+=1

        return count
        