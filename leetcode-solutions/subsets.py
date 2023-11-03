class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start,stack):
            #if find solution add it to result
            res.append(stack[:])
            #iterate over all possible candidates
            for i in range(start,len(nums)):
                    #try this partial candidate
                    stack.append(nums[i])
                    #given the candidate explore further
                    backtrack(i+1,stack)
                    #remove candidate
                    stack.pop()
        res=[]
        stack = []
        backtrack(0,stack)
        return res

        