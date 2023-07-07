t = int(input())

def solve(n,a):
    i = 0
    j = n-1
    while i<j:
        #if they are equal remove any
        if a[i]==a[j]:
            a.pop(i)
            j-=1
            #else remove the smallest element
        elif abs(a[i]-a[j])<=1:
            if a[i]<a[j]:
                a.pop(i)
                j-=1
            else:          
                break
        i+=1
        

        
        
    if len(a)==1:
        print('YES')
    else:
        print('NO')


for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    solve(n,a)