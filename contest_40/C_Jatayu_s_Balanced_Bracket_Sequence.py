def solve():
    n = int(input())
    s = input()
    ans = 0
    for i in range(2*n):
        if s[i] == "(" and s[i+1] == ")":
            ans += 1

    print(n-ans+1)

for _ in range(int(input())):
    solve()
