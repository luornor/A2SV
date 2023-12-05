import sys
import threading

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = list(map(int,input().split()))
        s = input()
        graph = {i+1:[] for i in range(n)}
        for i in range(n-1):
            graph[p[i]].append(i+2)
        visited = set()
        ans = 0
        def dfs(node):
            nonlocal ans
            count=1 if s[node-1]=='B' else -1
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    right = dfs(neighbour)
                    count+=right
            if count==0:
                ans+=1

            return count
        
        for i in range(1,n+1):
            if i not in visited:
                dfs(i)
        print(ans)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()