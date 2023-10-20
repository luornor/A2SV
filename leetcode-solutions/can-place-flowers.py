class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        #check for adjacent 
        count=0
        # if len(flowerbed)==1 and flowerbed[0]==0:
        #     return n==len(flowerbed)

        # if n==0:
        #     return True
        flowerbed=[0]+flowerbed+[0]
        r=1
        while r<len(flowerbed)-1:
            if flowerbed[r-1]==0 and flowerbed[r]==0 and flowerbed[r+1]==0:
                flowerbed[r]=1
                n-=1

            
            r+=1
        

        return n<=0
            
            


        