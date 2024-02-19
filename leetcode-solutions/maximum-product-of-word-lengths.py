class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        bitmask = [0]*(len(words))

        for i in range(len(words)):
            for c in words[i]:
                bitmask[i] |= 1<<(ord(c)-ord('a'))
        

        for i in range(len(words)):
            for j in range(len(words)):
                if not bitmask[i] & bitmask[j]:
                    ans = max(ans,len(words[i])*len(words[j]))
        
        return ans 
        