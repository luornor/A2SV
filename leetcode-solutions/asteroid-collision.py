class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            while stack and asteroids[i]<0 and stack[-1]>0:
                collide = asteroids[i]+stack[-1]
                if collide<0:
                    stack.pop()
                elif collide>0:
                    asteroids[i]=0
                else:
                    asteroids[i]=0
                    stack.pop()
            if asteroids[i]!=0:
                stack.append(asteroids[i])
        return stack