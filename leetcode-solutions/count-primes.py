class Solution:
    def countPrimes(self, n: int) -> int:
          
        marked = [False]* n
        
        count=0
        for i in range(2,n):
            if not marked[i]:
                for j in range(i*i,n,i):
                    marked[j]=True
                count+=1
                    
                
        return count