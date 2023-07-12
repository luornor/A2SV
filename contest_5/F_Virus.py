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
    
    houses = n
    protected = 0
    saved = 0
    for i in range(len(gaps)):
        gap_size = gaps[i] - 2*protected
        if gap_size > 2:
            saved += gap_size-1
            protected += 2
        else:
            if gap_size == 1:
                saved += 1
                protected += 1
            if gap_size==2:
                saved += 1
                protected += 1
    #minimun number of houses protected
    print(houses-saved)
    

for _ in range(t):
    solve()


