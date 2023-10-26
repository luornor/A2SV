class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        count = []

        for i in range(len(s)):
            if stack and stack[-1]==s[i]:
                count.append(count[-1]+1)
                stack.append(s[i])
            else:
                stack.append(s[i])
                count.append(1)

            if count[-1]==k:
                for _ in range(k):
                    stack.pop()
                    count.pop()
                

        
        return ''.join(stack)
        