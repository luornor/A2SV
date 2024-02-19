def solve():
    n,m = map(int, input().split())
    
    maze = []
    for _ in range(n):
        maze.append(input())


t = int(input())
for _ in range(t):
    print(solve())