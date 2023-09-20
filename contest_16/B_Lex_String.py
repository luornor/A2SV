def solve(a,b,n,m,k):
    c = ''
    l = 0
    r=0
    count_a=0
    count_b=0
    a=sorted(a)
    b=sorted(b)
    while l<n and r<m:
        if (a[l]<b[r] and count_a<k) or count_b==k:
            c+=a[l]
            count_a+=1
            count_b=0
            l+=1
        else:
            c+=b[r]
            count_b+=1
            count_a=0
            r+=1

    print(c)
    
    
        
    

t = int(input())
for _ in range(t):
    n,m,k = map(int,input().split())
    a = input()
    b = input()
    solve(a,b,n,m,k)