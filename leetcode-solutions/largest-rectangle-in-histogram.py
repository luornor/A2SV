class Solution:
    def largestRectangleArea(self, arr: List[int]) -> int:
        n = len(arr)
        stack = []
        next_smaller = [0]*n
        #next smaller left
        for i in range(n):
                
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if stack:
                next_smaller[i] = stack[-1]+1
            else:
                next_smaller[i] = 0

            stack.append(i)
        
        previous_smaller = [0]*n
        stack = []
            
        #previous smaller right
        for i in range(n-1,-1,-1):

            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if stack:
                previous_smaller[i] = stack[-1]-1
            else:
                previous_smaller[i] = n-1
            
            stack.append(i)

        res = 0
        # print(next_smaller)
        # print(previous_smaller)
        for i in range(n):
            res = max(res, (previous_smaller[i]-next_smaller[i]+1)*arr[i])

        return res