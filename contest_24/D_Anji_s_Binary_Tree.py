from collections import defaultdict
import sys
import threading


def main():
    t = int(input())
    for _ in range(t):
        n=int(input())
        s = input()
        s = list(s)
        graph = defaultdict(list)
        for i in range(n):
            l,r = map(int, input().split())
            graph[i+1].append(l)
            graph[i+1].append(r)

        def dfs(node,count):     
            if s[node-1]=='U' and node!=1:
                if graph[node][0]!=0:
                    s[node-1]='L'
                    return dfs(graph[node][0],count+1)

                if graph[node][1]!=0:
                    s[node-1]='R'
                    return dfs(graph[node][1],count+1)              
            #if char is L and is no left change it
            if s[node-1]=='L' and graph[node][0]==0:
                s[node-1]='R'
                return dfs(graph[node][1],count+1)

            if s[node-1]=='R' and graph[node][1]==1:
                s[node-1]='L'
                return dfs(graph[node][0],count+1)

            

            return count


            
        print(dfs(1,0))

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()

