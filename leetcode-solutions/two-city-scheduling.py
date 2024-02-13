class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res = 0
        n = len(costs)
        
        diffs = []
        for i,cost in enumerate(costs):
            diffs.append((abs(cost[0]-cost[1]),i))

        diffs.sort(reverse=True) 
        A = 0
        B = 0

        for i in range(n):
            diff, idx = diffs[i]
            if A < n // 2 and B < n // 2:
                if costs[idx][0] < costs[idx][1]:
                    res += costs[idx][0]
                    A += 1
                else:
                    res += costs[idx][1]
                    B += 1
            elif A < n // 2:
                res += costs[idx][0]
                A += 1
            else:
                res += costs[idx][1]
                B += 1

        return res
                

        