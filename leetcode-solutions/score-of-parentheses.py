class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        stack = []
       

        for item in s:
            if item=="(":
                stack.append(score)
                score=0
            else:
                if stack:
                    last_score = stack.pop()
                    score = last_score+max(2*score,1)

        return score

        