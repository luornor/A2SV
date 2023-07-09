t  = int(input())

def solve(n,a):
    b = a.copy()
    b.sort()
    res = []
    max_val = max(a)
    for i in range(n):
        if a[i]!=max_val :
            num = a[i]-max_val
        else:
            num = a[i]-b[n-2]
        res.append(num)

    return res


for _ in range(t):
    n = int(input())
    s = list(map(int,input().split()))
    ans = solve(n,s)
    print(*ans)

