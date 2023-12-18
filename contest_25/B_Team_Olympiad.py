def solve():
    n =int(input())
    t = list(map(int,input().split()))
    maths = []
    programming = []
    pe =[]
    for i in range(n):
        if t[i]==1:
            programming.append(i+1)
        elif t[i]==2:
            maths.append(i+1)
        else:
            pe.append(i+1)

    max_teams = min(len(programming), len(maths), len(pe))

    if max_teams == 0:
        print(0)
    else:
        print(max_teams)
        # Form teams
        for i in range(max_teams):
            print(programming[i], maths[i], pe[i])


solve()