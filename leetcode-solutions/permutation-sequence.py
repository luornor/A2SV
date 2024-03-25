class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        arr = list(range(1,n+1))
        
        res=[]
        perm = []
        def backtrack():
            #if find solution add it to result
            if len(res)==k:
                return 
            if len(perm)==n:
                res.append(perm[:])
                return
                
            
            #iterate over all possible candidates
            for num in arr:
                #try this partial candidate
                if num not in perm:
                    perm.append(num)
                #given the candidate explore further
                    backtrack()
                    #remove candidate
                    perm.pop()

        backtrack()

        ans = res[-1]
        return "".join([str(i) for i in ans])
        
        