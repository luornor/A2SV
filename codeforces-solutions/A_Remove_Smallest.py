t = int(input())

def solve(n,a):
    a.sort()
    for i in range(1,n):
        if abs(a[i]-a[i-1])>1:
           return 'NO'    
    return 'YES'
    
    # for i in range(n-1):
    #     if abs(a[i]-a[i+1])<=1:
    #        continue
    #     else:
    #         return 'NO' 
    # return 'YES'

    

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    print(solve(n,a))

    