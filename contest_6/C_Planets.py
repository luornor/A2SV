from collections import Counter
def solve(n,c,a):
    a.sort()
    orbit_counts = Counter(a) #count of orbits and their planets
    #3 2 1 2 2
    #1 2 2 2 3
    #vals = 1 2 3
    #counts = 1 3 1
    min_cost = 0 # Initialize minimum cost as 0
    for k,v in orbit_counts.items():
        if v < c:
            min_cost+=1*v
        else:
            min_cost+=c
    
    print(min_cost)
            
    

t = int(input())

for _ in range(t):
    n,c = map(int,input().split())
    a = list(map(int,input().split()))
    solve(n,c,a)