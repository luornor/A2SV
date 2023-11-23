def solve(a,n):
    ans = 0
    not_zero = False
    for i in range(n-1):
        if a[i]!=0:
            not_zero = True
            ans+=a[i]
        elif not_zero:
            ans+=1

    return ans
    
    
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    print(solve(a,n))