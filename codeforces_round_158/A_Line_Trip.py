def solve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = a[0]
    for i in range(1,n):
        ans = max(a[i]-a[i-1],ans)
    ans = max((x-a[-1])*2,ans)
    return ans
    

t = int(input())
for _ in range(t):
    print(solve())