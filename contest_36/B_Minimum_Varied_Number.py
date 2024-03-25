def solve():
    n = int(input())
    ans = ''

    for i in range(9,0,-1):
        if i<=n:
            ans+=str(i)
            n-=i
    
    return ans[::-1]

t = int(input())
for _ in range(t):
    print(solve())