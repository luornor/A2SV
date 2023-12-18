class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1

        queue = deque([('0000',0)])
        visited = set(deadends)
        

        while queue:
            lock,count = queue.popleft()
            if lock==target:
                return count

            next_states=[]
            for i in range(4):
                x = int(lock[i])
                x1 = (x+1)%10
                x2 = (x-1)%10
                num1 = lock[:i] + str(x1) + lock[i+1:]
                num2 = lock[:i] + str(x2) + lock[i+1:]
                next_states.extend([num1,num2])
         

            for state in next_states:
                if state not in visited:
                    visited.add(state)
                    queue.append((state,count+1))


        return -1