N = int(input())

def solve(n):
    print(f'{n[:2]}... {n}?')

for _ in range(N):
    n = input()
    solve(n)