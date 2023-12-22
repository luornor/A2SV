class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for u,v in edges:
            graph[u].append(v)
            indegree[v]+=1

        queue = deque()
        for node in range(n):
            if indegree[node]==0:
                queue.append(node)

        print(indegree)
        res = defaultdict(set)
        while queue:
            node = queue.popleft()

            for nei in graph[node]:
                indegree[nei]-=1
                
                for parent in res[node]:
                    res[nei].add(parent)

                res[nei].add(node)
                if indegree[nei]==0:
                    queue.append(nei)

                
        ans = []
        for i in range(n):
            ans.append(sorted(list(res[i])))

        return ans



        
        
        