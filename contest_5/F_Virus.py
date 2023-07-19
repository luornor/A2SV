"""
This may help


Step to do the virus problem 

- storing the size of each segment in an array( will be array of integers), let say the name is arr

- create a variable(infected) that taking care of the infected houses in each segment 

- until arr becomes empty or the max segment in the array less than infected, do these things 

1, choose the maximum number(max segment) and remove it from  arr
2, In the removed segment you are going to protect max(1, removed - 1 - inf)
3, add the number of protected houses to your answer
4, increment infected by 4, since you are going to lose 4 houses in each segment in each iteration


- finally you will have number of total protected houses that are accumulated in each iteration

"""
t = int(input())

def solve():
    #n is the number of houses on the circle
    # m is the number of houses that are initially infected
    n,m = map(int,input().split())
    # indexes of initially affected houses
    infected_houses = list(map(int, input().split()))
    infected_houses.sort()
    #gaps between infected houses
    segment = [(infected_houses[i] - infected_houses[i - 1] - 1) % n for i in range(m)]
    
    protected = 0   
    infected = 0
    while len(segment) > 0 and max(segment)>infected:
        idx = segment.index(max(segment))
        removed = segment.pop(idx)
        protected+=max(1, removed - 1 - infected)
        infected += 4
    print(n-protected)

for _ in range(t):
    solve()


