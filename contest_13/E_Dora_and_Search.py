def solve(a,n):
    l = 0
    r = n-1
    
    while l<n and a[l]==min(a):
        l+=1
    while r>0 and a[r]==max(a):
        r-=1
    if l<r:
        print(l+1,r+1)
    else:
        print(-1)
            
        
            

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    solve(a,n)