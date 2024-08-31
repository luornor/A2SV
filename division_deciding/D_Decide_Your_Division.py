def solve():
    n = int(input())
    operations = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        elif n % 3 == 0:
            n = (2 * n) // 3
        elif n % 5 == 0:
            n = (4 * n) // 5
        else:
            return -1
        operations += 1

    if n == 1:
        return operations
    else:
        return -1
    

for _ in range(int(input())):
    print(solve())