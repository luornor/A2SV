def solve():
    n = int(input())
    #factor of 2 and 5
    if n<1:
        return False
    while n % 2==0:
        n//=2

    while n % 5==0:
        n//=5

    return n==1
    

for _ in range(int(input())):
    if solve():
        print('YES')
    else:
        print('NO')
