# class Solution:
#     def longestPrefix(self, s: str) -> str:
#         a = 31 #base encode
#         mod = 10**9 + 7 #prime number
#         n = len(s)
#         def val(c):
#             return ord(c)-ord('a')+1

#         pre = 0
#         suff = 0
#         h = 1
#         ans=0
#         for i in range(n-1):
#             pre =  (pre*a + val(s[i])) % mod
#             suff = (suff + h* val(s[n-1-i]))%mod

#             h = (h * a) % mod
#             if pre==suff:
#                 ans = i+1
            
                    
#         return s[:ans]
class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        lps = [0]*n

        for i in range(1,n):
            j = lps[i-1]

            while j>0 and s[i] != s[j]:
                j = lps[j-1]
            
            if s[i]==s[j]:
                j+=1
            
            lps[i] = j
        
        # print(lps)
        return s[:lps[n-1]]
