def check(seg,n):
    return True  if (seg[0]!=1 and seg[-1]!=n) or (seg[-1]!=1 and seg[0]!=n) else False
        
    
def solve(a,n):
    min_a = 1
    max_a = n
    r = n - 1
    l = 0
    
    while l<r:
        if (a[l] != min_a and a[l]!=max_a) and (a[r]!=min_a and a[r]!= max_a):
            return f'{l+1} {r+1}'
            
        if a[l]==min_a :
            l+=1
            min_a+=1
            
        if a[l]==max_a:
            l+=1
            max_a-=1
        if a[r]==max_a:
            r-=1
            max_a-=1
        if a[r]==min_a:
            r-=1
            min_a+=1
        
       
    return -1
    
        

            

ans = 0
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    print(solve(a,n))