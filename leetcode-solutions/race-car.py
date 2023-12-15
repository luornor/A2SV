class Solution:
    def racecar(self, target: int) -> int:

        queue = deque([((0,1),0)])
        visited = set((0,1))
        while queue:
            (pos,speed),count = queue.popleft()
            
            if pos==target:
                return count
            
            #for accelerate don't go in negative direction or don't pass
            #the target more than two times
            new_pos=pos+speed
            new_speed=speed*2
            if 0<= new_pos <= 2*target and (new_pos,new_speed) not in visited:
                queue.append(((new_pos,new_speed),count+1))
                visited.add((new_pos,new_speed))

            #for reverse
            new_speed=-1 if speed>0 else 1
            
            if (pos,new_speed) not in visited:
                queue.append(((pos,new_speed),count+1))
                visited.add((pos,new_speed))
