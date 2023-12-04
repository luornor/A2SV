def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    distinct = set()
    suff = [0]*n
    for i in range(n-1,-1,-1):
        distinct.add(a[i])
        suff[i]=len(distinct)
    # print(suff)
    # print(distinct)
    for _ in range(m):
        l= int(input())
        print(suff[l-1])

            
    

solve()