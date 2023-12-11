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
    graph = defaultdict(list)
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    for node in graph:
        graph[node].sort(key=sequence.index)
    queue = deque([1])
    visited = set()
    res = []
    while queue:
        node = queue.popleft()
        if node in visited:
            break
        visited.add(node)
        res.append(node)
        for nei in graph[node]:
            if nei not in visited:
                queue.append(nei)

    if sequence == res:
        print('Yes')
    else:
        print('No')


sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()