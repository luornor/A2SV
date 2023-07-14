class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort()
        k = len(piles)//3
        res= 0
        for i in range(k,len(piles),2):
            res+=piles[i]
            print(res)

        return res