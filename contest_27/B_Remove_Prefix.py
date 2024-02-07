

def solve():
    n = int(input())
    a = list(map(int,input().split()))
    l = 0
    r = 0
    
    seen = set()
    while r<n:
        if a[r] not in seen:
            seen.add(a[r])
            r+=1
        else:
            seen.remove(a[l])
            l+=1
       
    return n-len(seen)

t = int(input())
for _ in range(t):
    print(solve())