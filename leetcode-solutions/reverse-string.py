class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #recursion
        def reverse(l,r,s):
            if l>=r:
                return 
            s[l],s[r]=s[r],s[l]

            reverse(l+1,r-1,s)
        l=0
        r=len(s)-1
        
        reverse(l,r,s)
        
        
