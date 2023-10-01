def solve(a,b):
    d=min(a,b)
    ans=min(d,(a+b)//4)
    print(ans)


t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    solve(a,b)