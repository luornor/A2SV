class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count =0
        n = x ^ y
        while n:
            if 1 & n:
                count+=1
            n>>=1
            
        return count
    

    

