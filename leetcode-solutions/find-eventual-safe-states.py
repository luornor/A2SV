class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        #count incoming egdes
        count = defaultdict(int)
        
        #reverse all edges
        adj = defaultdict(list)
        for i,nei in enumerate(graph):
            for num in nei:
                adj[num].append(i)
                count[i]+=1
                
                
        queue = deque()
        for node in range(len(graph)):
            if count[node]==0:
                queue.append(node)
        
        res = []
        while queue:
            node = queue.popleft()

            res.append(node)

            for nei in adj[node]:
                count[nei]-=1
                if count[nei]==0:
                    queue.append(nei) 

        
        return sorted(res)
        
        