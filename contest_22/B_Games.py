def solve():
    n = int(input())
    teams = []
    
    for _ in range(n):
        colors = list(map(int,input().split()))
        teams.append(colors)

    count =0
    for i in range(n):
        for j in range(i+1,n):
            if teams[i][1]==teams[j][0]:
                count+=1
            if teams[i][0]==teams[j][1]:
                count+=1
    return count





    
print(solve())
