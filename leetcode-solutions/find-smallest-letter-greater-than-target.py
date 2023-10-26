class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        stack = []
        l = 0
        r = len(letters)-1
        ans = letters[0]
        while l<=r:
            m = (l+r)//2
            if target==letters[m]:
                l=m+1
            elif target>letters[m]:
                l=m+1
            else:
                ans =  letters[m]
                r=m-1
        return ans



        