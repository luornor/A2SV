def solve(n,m,v,types):
    u = sorted(v)
    #6 4 2 7 2 7--v
    #2 2 4 6 7 7--u
    #2 3 6 types
    ans  = 0
    for num in types:
        if num==1:
            ans = sum(v[2:3])
    print(ans)

n = int(input())
v = list(map(int,input().split()))
m = int(input())

for _ in range(m):
    types = list(map(int,input().split()))
    solve(n,m,v,types)    