n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

#2 2 5 6 i
# 3 4 6 8 j
# ans 2 2 3 4
def solve(a,b,n,m):
    res = []
    j = 0
    for i in range(m):
        while j < n and a[j]<b[i]:
            j+=1
        res.append(j)   

    print(*res)
    


solve(a,b,n,m)