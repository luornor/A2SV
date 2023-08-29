class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = [0]*(len(self.nums))
        
        self.prefix[0] = self.nums[0]
        for i in range(1,len(self.nums)):
            self.prefix[i] =self.nums[i] + self.prefix[i-1]
        

    def sumRange(self, left: int, right: int) -> int:
        res = 0
        if left==0:
            return self.prefix[right]
        else:
            return self.prefix[right]-self.prefix[left-1]
       


        # return sum(self.nums[left:right+1])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)