def numRescueBoats(people,limit):
        
        people.sort()
        # 1 2 2 3
        l = 0
        r = len(people)-1
        res = 0
        while l <= r:
            weight_sum = people[l]+people[r]
            if weight_sum<=limit:
                r-=1
                l+=1
                res+=1
            else:
                r-=1
                res+=1
            
        return res