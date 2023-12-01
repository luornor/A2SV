
from collections import defaultdict
import sys
sys.setrecursionlimit(2000)
def dfs(num,graph):
    if not num:
        return 0
    ans = 0
    for x in graph[num]:
        ans = max(ans,dfs(x,graph))

    return ans+1

    

def solve():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))

    tree = defaultdict(list)
    for i,val in enumerate(arr):
        if val!=-1:
            tree[val].append(i+1) 

    group = 0
    for i,val in enumerate(arr):
        if val==-1:
            group =max(group,dfs(i+1,tree))


    return group

print(solve())