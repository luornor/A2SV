def solve():
    n = int(input())
    a = list(map(int,input().split()))

    arr = sorted((a,i) for i,a in enumerate(a))
    

t = int(input())
for _ in range(t):
    print(solve())
