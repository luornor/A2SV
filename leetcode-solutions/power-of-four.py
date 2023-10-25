class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # if n<1:
        #     return False
        # while n>0:
        #     if n==1:
        #         return True
        #     n=n/4
        # return False
        #base case
        if n<1:
            return False
        if n==1:
            return True
        return self.isPowerOfFour(n/4)

        