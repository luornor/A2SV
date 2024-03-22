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
        needle_hash =haystack_hash = 0

        ref = ord('a')
        for i in range(m):
            encode_needle = ord(needle[i])-ref+1
            encode_haystack = ord(haystack[i])-ref+1
            needle_hash = (a*needle_hash+encode_needle)%mod
            haystack_hash = (a*haystack_hash+encode_haystack)%mod

        for  i in range(n-m+1):
            if needle_hash==haystack_hash:
                if haystack[i:i+m]==needle:
                    return i
            if i<n-m:
                encode_haystack = ord(haystack[i])-ref+1
                next_char = ord(haystack[i+m])-ref+1
                haystack_hash=(a*(haystack_hash-encode_haystack*h) + next_char )%mod
                
                if haystack_hash<0:
                    haystack_hash+=mod

        return -1

        

        