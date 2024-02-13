
def solve():
    n,k =map(int, input().split())
    a = list(map(int, input().split()))
    
    count = 1
    res = 0
    for i in range(1,n):
        if 2*a[i]> a[i-1]:
            count+=1
        else:
            count=1
        if count>k:
            res+=1
        

    return res





t = int(input())
for _ in range(t):
    print(solve())