class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u,v in prerequisites:
            graph[v].append(u)

        
        #build graph
        #count incoming edges
        queue = deque()
        count = defaultdict(int)
        for k,v in graph.items():
            for nei in v:
                count[nei]+=1

        for i in range(numCourses):
            if count[i]==0:
                queue.append(i)
        # print(queue)
        ans = []
        while queue:
            u= queue.popleft()
            
            ans.append(u)
            
            for nei in graph[u]:
                count[nei]-=1
                if count[nei]==0:
                    queue.append(nei)

        if len(ans) != numCourses:
            return []
        return ans