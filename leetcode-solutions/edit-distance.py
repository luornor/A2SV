class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def dp(i,j):
            #insert remaining letters in word2
            if i==len(word1):
                return len(word2)-j
            #delte remainig letters in word1
            if j==len(word2):
                return len(word1) - i
            if (i,j) in memo:
                return memo[(i,j)]
            if word1[i]==word2[j]:
                return dp(i+1,j+1)

            insert = dp(i,j+1) + 1
            delete = dp(i+1,j) +1
            replace = dp(i+1,j+1) +1

            memo[(i,j)] = min(insert,delete,replace)

            return memo[(i,j)]
    


        return dp(0,0)