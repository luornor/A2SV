class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #"ababcbacadefegdehijhklij"
        # each letter apears in at most one part
        #store last index of each character in the string
        start = 0
        end = 0
        res = []
        for i in range(len(s)):
            end=max(end, s.rindex(s[i]))
            if i==end:
                res.append(end-start+1)
                start=i+1

        return res
            

