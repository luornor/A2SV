class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        unique_chars = set()
        max_lenght = 0
        while end < len(s):
            if s[end] not in unique_chars:
                unique_chars.add(s[end])
                end+=1
                max_lenght = max(max_lenght,end-start)
                
            else:
                unique_chars.remove(s[start])
                start+=1

        return max_lenght