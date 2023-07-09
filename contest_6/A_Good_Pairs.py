t = int(input())
# |ai-ak|+|ak-aj|=|ai-aj|,
# abs(a[i]-abs(k))+ abs(a[k]-a[j])==abs(a[i]-a[j])
def solve(n,a):
    res = []
    
    res.append(a.index(min(a))+1)
    res.append(a.index(max(a))+1)
        
        
    print(*res)

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    solve(n,a)
