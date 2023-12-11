from heapq import heapify, heappop


def solve(s):
    lower = []
    upper = []
    res = ''
    for i,char in enumerate(s):
        if char=='B' and upper:
            upper.pop()
        elif char=='b' and lower:
            lower.pop()
        if char.isupper() and char!='B':
            upper.append((i,char))
        elif char.islower() and char!='b':
            lower.append((i,char))
    upper+=lower
    upper.sort()
    for i,char in upper:
        res+=char
        
    return res

t = int(input())

for _ in range(t):
    s = input()
    print(solve(s))
