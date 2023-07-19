t = int(input())

def solve():
    #n is the number of houses on the circle
    # m is the number of houses that are initially infected
    n,m = map(int,input().split())
    # indexes of initially affected houses
    infected_houses = list(map(int, input().split()))
    infected_houses.sort()
    #gaps between infected houses
    gaps = [(infected_houses[i] - infected_houses[i - 1] - 1) % n for i in range(m)]
    
    protected = 0   
    num_infected = 0
    protected = 0
    while len(gaps) > 0 and max(gaps)>num_infected:
        removed = gaps.pop(0)
        protected+=max(1, removed - 1 - num_infected)
        num_infected+=4
    print(n-protected)

for _ in range(t):
    solve()


