from collections import defaultdict, deque
import sys
import threading


def main():
    n = int(input())
    edges = []
    for _ in range(n-1):
        x, y = map(int, input().split())
        edges.append((x, y))

    sequence = list(map(int, input().split()))
    graph = defaultdict(set)
    for x, y in edges:
        graph[x].add(y)
        graph[y].add(x)

    # print(graph)
    if sequence[0]!=1:
        return 'No'

    l = 0
    r = 1
    while r<len(sequence) and l<r:
        if sequence[r] in graph[sequence[l]]:
            r+=1
        else:
            l+=1
        
    if r==len(sequence):
        return 'Yes'
    else:
        return 'No'

print(main())