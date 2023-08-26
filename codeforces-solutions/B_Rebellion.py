def solve(a,n):
   for i in range(n):
       for j in range(i+1,n):
           if i!=j:
                



t = int(input())
for _ in range(t):
    n  = int(input())
    a = list(map(int,input().split()))
    solve(a,n)