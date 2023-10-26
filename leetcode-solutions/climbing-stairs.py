class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}
        def memo(n):
            if n in mem:
                return mem[n]
        
            if n<4:
                return n
            else:
                result=memo(n-1) + memo(n-2)
                mem[n]=result 
    
            return mem[n]

        return memo(n)
