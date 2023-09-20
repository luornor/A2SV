def solve(n,s):
    if not s:
        print(0)
    
    l = 0
    r = n-1
    res = n
    while l<=r:
        if (s[l]=='0' and s[r]=='1') or (s[l]=='1' and s[r]=='0'):
            res-=2
            l+=1
            r-=1
        else:
            print(res)
            return

    print(res)


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    solve(n,s)