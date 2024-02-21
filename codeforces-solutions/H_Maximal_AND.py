from collections import defaultdict


def solve():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))

    res = ''

    for i in range(30, -1, -1):
        count = 0
        for j in range(len(a)):
            num = a[j]
            if num & (1<<i)==0:
                count+=1
            
        if count<=k:
            res+='1'
            k-=count
        else:
            res+='0'
           


    return int(res,2)
    
t = int(input())
for _ in range(t):
    print(solve())