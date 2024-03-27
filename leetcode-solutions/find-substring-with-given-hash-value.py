class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        s = s[::-1]
        n = len(s)
        window = 0
        for i in range(k):
            val = ord(s[i])-ord('a')+1
            window+=(val*pow(power,k-i-1,modulo))
            window %= modulo
        
        ans = ""
        if window==hashValue:
            ans = s[:k]

        h = pow(power,k-1,modulo)
        #-i-k
        
        for i in range(k, n):
            remove = ord(s[i-k])-ord('a')+1
            add = ord(s[i])-ord('a')+1
            window = (window - remove*h) % modulo
            window = (window*power + add) % modulo

            if window==hashValue:
                ans = s[i-k+1:i+1]

        return ans[::-1]

                
            
            
        