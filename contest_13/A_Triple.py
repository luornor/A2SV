from collections import defaultdict


def solve(a,n):
    ans = -1
    hmap = defaultdict(int)
    for num in a:
        hmap[num]+=1
        if hmap[num]>=3:
            ans = num
            break        
                        
    print(ans)
    
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    solve(a,n)