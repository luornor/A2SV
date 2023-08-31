class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        # #total number of beans
        total = sum(beans)
        ans = 0
        res = float('inf')
        n = len(beans)
        for i in range(n):
            ans=total-beans[i]*(n-i)
            res = min(ans,res)


        return res

       
        

