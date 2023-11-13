def solve(alice, bob):
    print('Alice') if max(alice)>=max(bob) else print('Bob')
    print('Bob') if max(bob)>=max(alice) else print('Alice')
  

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    solve(a,b)