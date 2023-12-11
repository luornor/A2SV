from collections import defaultdict
import sys
import threading

def main():
    n,m = map(int,input().split())
    cats = list(map(int,input().split()))
    graph = defaultdict(list)
    for _ in range(n-1):
        x,y = map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    visited = set()
    res=[0]
    def dfs(node,count):
        visited.add(node)
        if cats[node-1]==1:
            count+=1
        else:
            count=0

        if count>m:
            return
        isleaf = True
        for nei in graph[node]:
            if nei not in visited:
                isleaf=False
                dfs(nei,count)

        if isleaf:
            res[-1]+=1    
                

        return res[-1]

    print(dfs(1,0))
    

    


sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()