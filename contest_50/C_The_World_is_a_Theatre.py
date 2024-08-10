import math

def combination(n,k):
    if n<k:
        return 0
    
    return math.comb(n,k)

n,m,t = map(int,input().split())
total = 0
for boys in range(4,t):
    girls = t-boys
    
    if girls>=1 and girls<=m:
        boys_total =combination(n,boys)
        girls_total = combination(m,girls)

        total+= (girls_total*boys_total)

print(total)

