class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle==haystack:
            return 0

        a = 31 #base encode
        mod = 10**9 + 7 #prime number
        m= len(needle)
        n = len(haystack)
        if m>n:
            return -1

        h = pow(a,m-1)%mod
        needle_hash =0
        haystack_hash = 0

        ref = ord('a')
        for i in range(m):
            encode_needle = ord(needle[i])-ref+1
            encode_haystack = ord(haystack[i])-ref+1
            needle_hash = (needle_hash+encode_needle*pow(a,m-i-1))%mod
            haystack_hash = (haystack_hash+encode_haystack*pow(a,m-i-1))%mod
        
    

        if needle_hash==haystack_hash:
            return 0

        for i in range(m,n):
            remove = ord(haystack[i-m])-ref+1
            add = ord(haystack[i])-ref+1
            haystack_hash=(a*(haystack_hash-remove*h) + add )%mod

            if haystack_hash==needle_hash:
                return i-m+1
                
        return -1

        

        