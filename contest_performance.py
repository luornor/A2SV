"""

Vasya considers a coder's performance in a contest amazing in two situations: 
he can break either his best or his worst performance record. 
First, it is amazing if during the contest the coder earns strictly more points that he earned on each past contest. 
Second, it is amazing if during the contest the coder earns strictly less points that he earned on each past contest. 
A coder's first contest isn't considered amazing.
100 50 200 150 200
Now he wants to count the number of amazing performances the coder had throughout his whole history of participating in contests.
"""
N = int(input())


def solve(x):
    n = [int(x[i]) for i in range(len(x))]
    amazing = 0
    
    for i in range(1,len(n)):
        if check_for_less(n[i],n[:i]):
            amazing+=1
        elif check_for_more(n[i],n[:i]):
            amazing+=1
    
    print(amazing)

def check_for_less(num,list):
    return all(num < x for x in list)

def check_for_more(num,list):
    return all(num > x for x in list)

x = input().split()
solve(x)
