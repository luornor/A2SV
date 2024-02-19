def solve():
    x = int(input())
    
    y = 0
    while not (x & y) or not x^y:
        y+=1
    
    return y


t = int(input())

for _ in range(t):
    print(solve())