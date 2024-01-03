class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        insertions = 0

        i = 0
        while i < len(s):
            c = s[i]
            if c == '(':
                stack.append(c)
            elif c == ')':
                if i < len(s) - 1 and s[i + 1] == ')':
                    i += 1
                    if stack:
                        stack.pop()
                    else:
                        insertions += 1
                else:
                    if stack:
                        stack.pop()
                        insertions += 1
                    else:
                        insertions += 2
            i += 1

        insertions += len(stack) * 2
        return insertions
