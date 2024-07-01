def check(k, a):
    res = 0
    for i in range(len(a) - 1):
        res += min(k, a[i + 1] - a[i])
    res += k
    return res

def solve():
    n, h = map(int, input().split())
    a = list(map(int, input().split()))
    l, r = 1, h
    while l <= r:
        mid= (l+r)//2
        if check(mid, a)>=h:
            r = mid - 1
        else:
            l = mid + 1

    return l


for _ in range(int(input())):
    print(solve())
    


        
