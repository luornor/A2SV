from collections import defaultdict


def solve():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))

    bitmask = [0]*31
    res = 0
    for num in a:
        for i in range(31):
            if num & 1:
                bitmask[i]+=1
            num>>=1
    
    for i in range(30,-1,-1):
        curr = n-bitmask[i]
        
        if k >= curr:
            res+=pow(2,i)
            k -= curr

    return res
    
t = int(input())
for _ in range(t):
    print(solve())