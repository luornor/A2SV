s = input()
stack = []
n = len(s)
end = n-1
for i in range(n):
    if s[i] == '(':
        for j in range(end, i, -1):
            if s[j] == ')':
                end = j - 1
                stack.append(i)
                stack.append(j)
                break
if stack:
    print(1)
    print(len(stack))
    stack.sort()
    for idx in stack:
        print(idx+1,end=' ')
else:
    print(0)
# print(stack)
