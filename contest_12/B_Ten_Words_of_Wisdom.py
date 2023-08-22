def solve(grid):
    potential = []
    i = 1
    for a,b in grid:
        if a<=10:
            potential.append([i,b])
        i+=1
    winner = 0
    max_idx = 0
    # print(potential)
    for item in potential:
        if item[1] > winner:
            winner = item[1]
            max_idx = item[0]
        
    print(max_idx)
        




t = int(input())
for _ in range(t):
    n = int(input())
    game  = []
    for _ in range(n):
        a = list(map(int,input().split()))
        game.append(a)
    solve(game)
