    
def solve():
    n = int(input())
    if n==1:
        return 2
    if n % 3 == 0:
        return n // 3
    elif n % 3 == 1:
        return (n // 3) + 1  
    else:
        return (n // 3) + 1
    



for _ in range(int(input())):
    print(solve())