def solve(boys,a,girls,b):
    a.sort()
    # 1 4 6 2
    #1 2 4 6
    #5 1 5 7 9
    #1 5 5 7 9
    b.sort()
    ans = 0
    l = 0
    r = 0
    
    while l < boys and r < girls:
        if abs(a[l] - b[r]) <= 1:
            ans += 1
            l += 1
            r += 1
        elif a[l] < b[r]:
            l += 1
        else:
            r += 1

    print(ans)

n = int(input())#boys
a = list(map(int,input().split()))

m = int(input())#girls
b = list(map(int,input().split()))
solve(n,a,m,b)
