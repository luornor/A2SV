class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        mat = [[False]*numCourses for _ in range(numCourses)]

        #every course is a prerequisite of itself
        for i in range(numCourses):
            mat[i][i]=True

        for u,v in prerequisites:
            mat[u][v]=True

        for i in range(numCourses):
            for j in range(numCourses):
                for k in range(numCourses):
                    mat[j][k] = mat[j][k] or (mat[j][i] and mat[i][k])
        res = []
        for k,v in queries:
            res.append(mat[k][v])

        return res
