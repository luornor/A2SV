class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))

        queue = [(0,k)]
        heapify(queue)
        visited = set()
        while queue:
            w,node = heappop(queue)

            visited.add(node)
            if len(visited)==n:
                return w

            for nei,wei in graph[node]:
                if nei not in visited:
                    heappush(queue,(wei+w,nei))

        return -1

        