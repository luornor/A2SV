"""
This problem can be solved by using a greedy approach, 
moving from the end of the line towards the beginning. 
For each person, we keep track of the minimum index of a person
that can be killed by all the previous people in the line. 
If the range of the current person's claw is wider than that, we update the index.
In this function, the variable min_index keeps track of the minimum index
of a person who can be killed by any of the previous people. 
We traverse the list in reverse order. 
For each person, if their index is less than min_index, 
we increment the count of alive people. 
Then we update min_index to be the minimum of min_index and the index of the farthest person 
the current person can kill.
"""
def solve(n,l):
    alive = 0 #number of people alive
    min_idx = n
    for i in range(n - 1, -1, -1):
        if i < min_idx:
            alive += 1
        min_idx = min(min_idx, i - l[i])
    print(alive)
                



n = int(input())
l = list(map(int,input().split()))
solve(n,l)