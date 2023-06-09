def nearestValidPoint(x: int, y: int, points: list[list[int]]) -> int:
    min_dist = float('inf')
    min_index = -1
    for i,point in enumerate(points):
        distance = abs(x-point[0])+ abs(y-point[1])
        if (point[0]==x or point[1]==y) and distance<min_dist:
            min_dist = distance
            min_index = i
    if min_index==-1:
        return min_index
    
    return min_index




x=1
y=1
# points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
# points = [[3,4]]
# points = [[2,3]]
points = [[1,1],[1,1]]
print(nearestValidPoint(x,y,points))