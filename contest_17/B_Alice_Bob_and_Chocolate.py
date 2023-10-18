def solve(n,arr):
    Acnt, Bcnt = 0, 0
    l, r = 0, n - 1
    Asum, Bsum = arr[l], arr[r]
    
    while l <= r:
        if Asum <= Bsum:
            Asum += arr[l + 1]
            l += 1
            Acnt += 1
        else:
            Bsum += arr[r - 1]
            r -= 1
            Bcnt += 1
    
    print(Acnt,Bcnt,end=" ")

n = int(input())
arr = list(map(int, input().split()))

solve(n,arr)
