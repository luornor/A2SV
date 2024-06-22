def solve():
    n = int(input())
    ans = ''

    for i in range(9,0,-1):
        if i<=n:
            ans+=str(i)
            n-=i
    
    return ans[::-1]

for _ in range(int(input())):
    print(solve())