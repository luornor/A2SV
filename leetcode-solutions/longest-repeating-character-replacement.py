class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        res = 0
        char_count = {}
        n = len(s)
        while right< n:
            char_count[s[right]] = char_count.get(s[right],0)+1
            if k<right-left+1 - max(char_count.values()):
                char_count[s[left]]-=1
                left+=1
            res = max(res,right-left+1)
            right+=1
            
            
            
            
                


            
        return res
            
            


        return max_len


