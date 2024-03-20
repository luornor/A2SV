class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        MOD = 10**9 + 7
        for u,v,t in roads:
            graph[u].append((v,t))
            graph[v].append((u,t))

        queue = [(0,0)]
        heapify(queue)
        visited = set()
        
        distance = [0]*n
        while queue:
            dist,node = heappop(queue)

            if node in visited:
                continue

            distance[node]=dist

            visited.add(node)
            for nei,time in graph[node]:
                if nei not in visited:
                    heappush(queue,(time+dist,nei))


        memo = {}
        def dp(node,t):
            if node in memo:
                return memo[node]

            if node==0:
                return 1

            ways = 0
            for nei,time in graph[node]:
                if t+time+distance[nei]==distance[n-1]:
                    ways+=dp(nei,t+time)

            memo[node]=ways

            return memo[node]

        # print(distance)
        return dp(n-1,0) % MOD
            