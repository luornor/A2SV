from collections import Counter
def solve(n,c,a):
    orbit_counts = Counter(a) #count of orbits and their planets
    # orbit_counts = {}  # Dictionary to store the count of planets for each orbit
    # for orbit in a:
    #     orbit_counts[orbit] = orbit_counts.get(orbit, 0) + 1
    min_cost = float('inf')  # Initialize minimum cost as infinity
    for count in orbit_counts.values():
        # Cost of using the first machine to destroy all planets in the current orbit
        cost_first_machine = count  
        cost_second_machine = (count) + c  
        min_cost = min(min_cost, cost_first_machine, cost_second_machine)

    print(min_cost)
            
    

t = int(input())

for _ in range(t):
    n,c = map(int,input().split())
    a = list(map(int,input().split()))
    solve(n,c,a)