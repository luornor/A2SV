# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
   

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        while l<=r:
            pick = (l+r)//2
            ans = guess(pick)
            if ans<0:
                r=pick-1
            elif ans>0:
                l=pick+1
            else:
                return pick
