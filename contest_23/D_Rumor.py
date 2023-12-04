from collections import defaultdict
import sys
import threading

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
 
def main():
    n,m = map(int, input().split())
    gold = list(map(int, input().split()))
    graph = defaultdict(list)
    visited = set()
    for _ in range(m):
        x,y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    # print(graph)
    def dfs(node):
        bribe=gold[node-1]
        visited.add(node)
        for friend in graph[node]:
            if friend not in visited:
                bribe = min(bribe,dfs(friend))
        return bribe
    total = 0
    for i in range(1,n+1):
        if i not in visited:
            total+=dfs(i)
    
    
    print(total)

main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
