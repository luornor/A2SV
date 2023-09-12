class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        que = deque()
        time = 0
        for i,ticket in enumerate(tickets):
            que.append((i,ticket))

        while True:
            #serve the person at the front of the que
            i,ticket = que.popleft()
            #if the person still has some more tickets to buy
            if ticket>1:
                que.append((i,ticket-1))
            #if we get to the  person
            elif i==k:
                # increment the time again becos we need to get to zero.
                time+=1 
                break
            time+=1 

        return time




           
