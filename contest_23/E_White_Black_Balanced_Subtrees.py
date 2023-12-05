import sys
import threading



def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nodes = list(map(int,input().split()))
        s = input()
        graph = {i+1: [] for i in range(n)}
        for i in range(n-1):
            graph[nodes[i]].append(i+2)

        visited = set()
        res=0   
        def dfs(node):
            nonlocal res
            count=0
            visited.add(node)
            if s[node-1]=='B':
                count=1
            else:
                count=-1
            for neighbour in graph[node]:
                if neighbour not in visited:
                    temp=dfs(neighbour)
                    count+=temp
            if count==0:
                res+=1
            return count
        
        for i in range(1,n+1):
            if i not in visited:
                dfs(i)

        print(res)

    

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()

