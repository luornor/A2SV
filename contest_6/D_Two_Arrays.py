def solve(a,b,n):
    if a==b:
        print('YES')
    else:
        a.sort()
        b.sort()
        
        for i in range(n):
            if a[i]==b[i]:
                continue
            else:
                a[i]+=1
        if a==b:
            print('YES')
        else:
            print('NO')


t = int(input())

for _ in range(t):
    n= int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    solve(a,b,n)