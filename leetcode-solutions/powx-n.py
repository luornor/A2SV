class Solution:
    def myPow(self, x: float, n: int) -> float:
        #recursion 
        def power(x,n):
            if n==0:
                return 1
            elif n%2==0:
                y= self.myPow(x,n//2)
                return y*y
            else:
                return x*self.myPow(x,n-1)

        ans=power(x,abs(n))
        if n<0:
            return 1/ans
        return ans
        