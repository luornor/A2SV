class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        df = [0] * (len(s)+2)

        for l,r,k in shifts:
            d = 1 if k==1 else -1
            df[l]+=d
            df[r+1]-=d

        for i in range(1,len(df)):
            df[i]+= df[i-1]

        res = ''
        for i in range(len(s)):
            pos = ord(s[i])-ord('a')
            shift = df[i]
            char = (pos+shift) % 26
            res+=chr(char+ord('a')) 

        # print(s)

        return res

        