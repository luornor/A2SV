class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        stack = []
        n = len(arr)
        
        MOD = 10**9 + 7
       
        left = [0] * n
        right = [0] * n

        for i in range(n):
            count = 1
            while stack and arr[stack[-1]]>arr[i]:
                idx = stack.pop()
                count+=left[idx]

            left[i]=count
            stack.append(i)

        stack = []
        for i in range(n-1,-1,-1):
            count=1
            while stack and arr[stack[-1]]>=arr[i]:
                idx = stack.pop()
                count+=right[idx]

            right[i]=count
            stack.append(i)

        total_sum = 0
        for i in range(n):
            total_sum=(total_sum+left[i]*right[i] * arr[i])%MOD

        return total_sum