def is_possible(h,arr,x):
    water = 0
    for num in arr:
        if h > num:
            water+=h-num

    return water>x

def solve():
    n,x = map(int,input().split())
    heights = list(map(int,input().split()))

    l, r = 1, 10**10
    while l< r-1:
        mid = (l + r) // 2

        if is_possible(mid, heights, x):
            r = mid 
        else:
            l = mid 

    return l

t = int(input())
for _ in range(t):
    print(solve())
     