class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        k = len(s1)
        #ab
        #"eidboaoo"
        start = 0
        end = k
        window = Counter(s2[:k])
        s1Count = Counter(s1)
        #check initial window for permutation
        if window==s1Count:
                return True
        while end<n:
            #slide window
            window[s2[start]]-=1
            window[s2[end]]+=1
            if window[s2[start]]==0:
                del window[s2[start]]
            #check condition after sliding
            if window==s1Count:
                return True
            end+=1
            start+=1
            
        return False

