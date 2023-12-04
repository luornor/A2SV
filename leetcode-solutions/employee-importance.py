"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        visited = set()
        imp = 0
        def dfs(id):
            nonlocal imp
            #if it has no subordinates
            visited.add(id)
            imp+=graph[id].importance
            for sub in graph[id].subordinates:
                if sub not in visited:
                    dfs(sub)
                
        graph = {employee.id: employee for employee in employees}

        # print(graph)
        
        dfs(id)
        return imp


        

        

        

        