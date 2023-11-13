def solve(m,p):
    

t = int(input())
for _ in range(t):
    m = int(input())#power of two size of permutation
    p = list(map(int,input().split()))
    solve(m,p)