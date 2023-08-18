def solve(n,a):
    a.sort()
    ans = 0
    if a[0]!=0:
        ans=2
    else:
        ans=1
    for i in range(n-1):
        if a[i]<i+1 and a[i+1]>= i+2:
            ans+=1

    print(ans)
    



t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    solve(n,a)