class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for num in tokens:
            if num not in '+-*/':
                stack.append(int(num))
            if stack:
                if num=='+':
                    first = int(stack.pop())
                    sec = int(stack.pop())
                    val = first+sec
                    stack.append(val)
                elif num=='*':
                    first = int(stack.pop())
                    sec = int(stack.pop())
                    val = first*sec
                    stack.append(val)
                elif num =='/':
                    first = int(stack.pop())
                    sec = int(stack.pop())
                    val = int(sec/first)
                    stack.append(val)
                elif num=='-':
                    first = int(stack.pop())
                    sec = int(stack.pop())
                    val = sec-first
                    stack.append(val)


        return stack[0]

        