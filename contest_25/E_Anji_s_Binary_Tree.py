from collections import defaultdict,deque


def solve():
    n = int(input())
    s = input()

    graph = defaultdict(list)
    for i in range(n):
        l,r = map(int,input().split())
    
        graph[i+1].append(l)
        graph[i+1].append(r)

    queue = deque([(1,0)])
    min_op = float('inf')

    while queue:
        node,count= queue.popleft()
        #at leaf node
        if graph[node][0]==0 and graph[node][1]==0:
            min_op = min(min_op,count)

        #increment count if it's different
        if graph[node][0] !=0 :
            if s[node-1]=='L':
                queue.append((graph[node][0],count))
            else:
                queue.append((graph[node][0],count+1))

        if graph[node][1] !=0 :
            if s[node-1]=='R':
                queue.append((graph[node][1],count))
            else:
                queue.append((graph[node][1],count+1))


    return min_op




t = int(input())
for _ in range(t):
    print(solve())