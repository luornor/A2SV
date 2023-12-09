class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i!=j:
                    x1,y1,r1 = bombs[i]
                    x2,y2,r2 = bombs[j]
                    distance = sqrt((x1-x2)**2 + (y1-y2)**2)
                    if distance<=r1:
                        graph[i].append(j)
                    

        def dfs(bomb):
            for nei in graph[bomb]:
                if nei not in visited: 
                    visited.add(nei)
                    dfs(nei)
                
        ans = 0
        for i in range(len(bombs)):
            visited=set([i])
            dfs(i)
            ans = max(ans,len(visited))

        return ans
