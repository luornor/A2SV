import math
for _ in range(int(input())):
    n = int(input())
    print(math.ceil(n/2))
    i = 2
    j = 3*n
    
    while i<j:
        print(i, j)
        i+=3
        j-=3
    
