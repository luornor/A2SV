def solve(a,n):
    count=0
    for i in range(n):
        for j in range(i+1,n):
            if a[i]<i+1<a[j]<j+1:
                count+=1
    
    

    print(count)

t = int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    solve(a,n)