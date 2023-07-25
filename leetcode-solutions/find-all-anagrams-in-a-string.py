class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        k = len(p)
        start = 0
        end = k
        res= []
        # Function to check if two frequency tables (hashmaps) are equal
        def is_anagram(freq1,freq2):
            return freq1==freq2

        # Create frequency tables for string p and the initial window in s
        freq_p = Counter(p)
        freq_window = Counter(s[:k])
        #cbaebabacd
        while start<n-k+1:
            # Check if the current window is an anagram of p
            if is_anagram(freq_window,freq_p):
                res.append(start)
            # Move the window by one character to the right
            if end<n:
                freq_window[s[start]]-=1
                if freq_window[s[start]] == 0:
                    del freq_window[s[start]]
                    
                freq_window[s[end]]+=1
                end+=1
            start+=1  
                      
        return res

        





