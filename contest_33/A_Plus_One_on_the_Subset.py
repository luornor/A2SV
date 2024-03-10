def solve():
    n = int(input())
    a = list(map(int,input().split()))
    maxx = max(a)
    minn = min(a)

    return maxx-minn

t = int(input())
for _ in range(t):
    print(solve())