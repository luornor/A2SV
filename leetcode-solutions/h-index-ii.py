class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l=0 
        r=len(citations)-1
        while l<=r:
            m=(l+r)//2
            #looking for maximum so eliminate minimum
            papers=len(citations)-m
            if papers==citations[m]:
                return papers
            elif papers>citations[m]:
                l=m+1
            else:
                r=m-1
        return len(citations)-l
        