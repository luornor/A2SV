class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        
        def kmp_search(s,pattern):

            s = pattern + '#' + s
            n = len(s)
            m = len(pattern)

            lps = [0]*n

            for i in range(1, n):
                j = lps[i-1]
                
                while j > 0 and s[i] != s[j]:
                    j = lps[j-1]
                
                if s[i] == s[j]:
                    j += 1
                
                if j == m:
                    return i-m
                    
                lps[i] = j
            
            return -1
        

        if kmp_search(a,b) !=-1:
            return 1

        k = len(b)//len(a)
        for i in range(k,k+3):
            
            if kmp_search(a*i,b) != -1:
                return i

        return -1


        

        
