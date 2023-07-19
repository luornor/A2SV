n = int(input())

a = list(map(int,input().split()))

def solve(n,a):
    a.sort()
    team = 0

    r = 0
    for l in range(n):
        while r<n and a[r]-a[l]<=5:
            team = max(team,r-l+1)
            r+=1

    print(team)




solve(n,a)