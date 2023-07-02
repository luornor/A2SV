t = int(input())

def solve(n,k,p):
    i = 0
    j = n-1
    while i<j:
        if abs(i-j)==k:
            p[i],p[j]= p[j],p[i]
            break
        i+=1
        j-=1
    

for _ in range(t):
    n,k = map(int,input().split())
    p = list(map(int,input().split()))
    print(solve(n,k,p))