def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    max_change = -1
    for ai,bi in zip(a,b):
        if bi> ai:
            return "NO"
            
        max_change = max(max_change, ai - bi)

    for i in range(n):
        t = max(a[i] - max_change, 0)
        if t != b[i]:
            return "NO"
    return "YES"


t = int(input())
for _ in range(t):
    print(solve())



