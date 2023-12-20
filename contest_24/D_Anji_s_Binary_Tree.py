from collections import defaultdict, deque
import sys
import threading


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        graph = defaultdict(list)
        for i in range(n):
            l, r = map(int, input().split())
            graph[i+1].append(l)
            graph[i+1].append(r)

        min_op = float('inf')
        queue = deque([(1, 0)])  # Start BFS from node 1 with count 0

        while queue:
            node, count = queue.popleft()

            if graph[node][0] == 0 and graph[node][1] == 0:
                min_op = min(min_op, count)
                

            if graph[node][0] != 0:
                if s[node-1] == 'L':
                    queue.append((graph[node][0], count))
                else:
                    queue.append((graph[node][0], count+1))

            if graph[node][1] != 0:
                if s[node-1] == 'R':
                    queue.append((graph[node][1], count))
                else:
                    queue.append((graph[node][1], count+1))

        print(min_op)

main()


# def main():
#     t = int(input())
#     for _ in range(t):
#         n=int(input())
#         s = input()
#         s = list(s)
#         graph = defaultdict(list)
#         for i in range(n):
#             l,r = map(int, input().split())
#             graph[i+1].append(l)
#             graph[i+1].append(r)

#         def dfs(node,count):   
#             nonlocal min_op  
#             if graph[node][0]==0 and graph[node][1]==0:
#                 min_op = min(min_op,count)
#                 return
        
#             #if the left node is L don't increment count 
#             if graph[node][0] !=0:
#                 if s[node-1]=='L':
#                     dfs(graph[node][0],count)
#                 else:
#                     dfs(graph[node][0],count+1)
#             if graph[node][1] !=0:
#                 if s[node-1]=='R':
#                     dfs(graph[node][1],count)
#                 else:
#                     dfs(graph[node][1],count+1)


#         min_op = float('inf')
#         dfs(1,0)
#         print(min_op)

        
# main()
# # sys.setrecursionlimit(1 << 30)
# # threading.stack_size(1 << 27)
# # main_thread = threading.Thread(target=main)
# # main_thread.start()
# # main_thread.join()