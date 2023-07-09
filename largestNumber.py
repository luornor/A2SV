class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        # [3,30,34,5,9]
        # 3,5,9,30,34
        #[9,909]
        #9099
        #9909
        nums = sorted(nums,reverse=True)
        n = len(nums)
        if all(num == 0 for num in nums):
            return '0'
        for i in range(n):
            for j in range(n-1):
                num1 = str(nums[j])
                num2 = str(nums[j+1])
                if int(num1+num2)<int(num2+num1):
                    nums[j],nums[j+1] = nums[j+1],nums[j]
        res = ""
        for ch in nums:
            res+=str(ch)

        return res


        

        
