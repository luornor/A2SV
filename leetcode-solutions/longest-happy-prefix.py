class Solution:
    def longestPrefix(self, s: str) -> str:
        a = 31 #base encode
        mod = 10**9 + 7 #prime number
        n = len(s)
        def val(c):
            return ord(c)-ord('a')+1

        pre = 0
        suff = 0
        h = 1
        ans=0
        for i in range(n-1):
            pre =  (pre*a + val(s[i])) % mod
            suff = (suff + h* val(s[n-1-i]))%mod

            h = (h * a) % mod
            if pre==suff:
                ans = i+1
            
                    
        return s[:ans]