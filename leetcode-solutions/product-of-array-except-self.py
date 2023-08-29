class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product = [1]*n
        prod = 1
        #multiply prefix for each element
        for i in range(n):
            product[i]=prod
            prod*=nums[i]
        prod = 1
        #multiply suffix for each element
        for j in range(n-1,-1,-1):
            product[j] *= prod
            prod *= nums[j]

        return product

        
