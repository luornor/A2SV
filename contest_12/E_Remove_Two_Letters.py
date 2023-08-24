def solve(s,n):
    repeated = 0
    for i in range(2,n):
        if s[i]==s[i-2]:
            repeated+=1
    print(n-1-repeated)


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    solve(s,n)

