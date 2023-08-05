import math

def solve(n,a):
    is_possible = False
    gcd_a = a[0]
    for num in a[1:]:
        gcd_a = math.gcd(gcd_a,num)
    
    if gcd_a<len(a):
        print('YES')
    else:
        print('NO')


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    solve(n,a)