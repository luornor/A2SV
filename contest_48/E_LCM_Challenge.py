from math import lcm
n = int(input())
if n < 3:
    print(n)
else:
    print( max(lcm(n,n-1,n-2), lcm(n,n-1,n-3), lcm(n-1,n-2,n-3),lcm(n,n-2,n-3)))
