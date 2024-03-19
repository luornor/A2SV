
from collections import defaultdict

def bootstrap(f, stack=[]):
    from types import GeneratorType
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
            if not stack:
                break
            to = stack[-1].send(to)
        return to
 
    return wrappedfunc



def solve():
    n = int(input())
    graph = defaultdict(list)
    flag = False
    for _ in range(n):
        a,b = map(int,input().split())
        
        graph[a].append(b)
        graph[b].append(a)

        if len(graph[a]) > 2 or len(graph[b]) > 2 or a==b:
            flag = True
    if flag:
        return "NO"

    color = [-1]*(n+1)
    @bootstrap
    def dfs(node):
        for neighbour in graph[node]:
            #already coloured
            if color[neighbour]!=-1:
                if color[node]==color[neighbour]:
                    return False
            else:
                #uncoloured
                color[neighbour] = 1 - color[node]
                if not dfs(neighbour):
                    return False

        return True


    for node in range(1,n+1):
        #not colored
        if color[node]==-1:
            color[node]=0
            if not dfs(node):
                return 'NO'

    return 'YES'


t = int(input())
for _ in range(t):
    print(solve())

    