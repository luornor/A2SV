import sys
import threading
from collections import defaultdict
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nodes = list(map(int,input().split()))
        s = input()
        graph = defaultdict(list)
        for i in range(n-1):
            graph[nodes[i]].append(i+2)
        res=[0]
        def dfs(node):
            count=0
            if s[node-1]=='B':
                count=1
            else:
                count=-1

            for neighbour in graph[node]:
                temp=dfs(neighbour)
                count+=temp

            if count==0:
                res[-1]+=1

            return count
        
        dfs(1)

        print(res[-1])

    

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()

