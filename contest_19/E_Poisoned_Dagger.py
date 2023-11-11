def how_much_damage(k, a):
    res = 0
    for i in range(len(a) - 1):
        res += min(k, a[i + 1] - a[i])
    res += k
    return res

def solve(a,h):
    l, r = 1, h
    while l <= r:
        mid= (l+r)//2
        if how_much_damage(mid, a)>=h:
            r = mid - 1
        else:
            l = mid + 1

    print(l)

t = int(input())

for _ in range(t):
    n, h = map(int, input().split())
    a = list(map(int, input().split()))
    solve(a,h)
    
