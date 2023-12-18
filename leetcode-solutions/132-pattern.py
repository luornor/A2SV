class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        #[3,1,4,2]
        #[-1,3,2,0]
        #nums[i] < nums[k] < nums[j].
        min_arr = [nums[0]]
        for i in range(1,len(nums)):
            min_arr.append(min(min_arr[i-1],nums[i]))
        
        print(min_arr)
        stack = []
        for j in range(len(nums)-1,-1,-1):
            while stack and stack[-1] <= min_arr[j]:
                stack.pop()
        
            if stack and stack[-1]<nums[j]:
                return True
            stack.append(nums[j])

        return False
