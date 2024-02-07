def solve():
    n = int(input())
    if n % 7==0:
        return n
    x = n%7
    y = 7-x
    z = n % 10
    if z+y<10:
        n+=y
    else:
        n-=x

    return n

t = int(input())
for _ in range(t):
    print(solve())