def solve():
    n = int(input())

    for r in range(2 * n):
        for c in range(n):
            if (r // 2 + c) % 2 == 0:
                print('##',end = '')
            else:
                print('..',end='')
        print()
    
t = int(input())
for _ in range(t):
    solve()