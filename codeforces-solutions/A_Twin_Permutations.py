t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))

    maxx = max(a)
    new = []
    for num in a:
        new.append(maxx-num+1)
    
    print(*new)