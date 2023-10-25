class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #Return the least weight capacity of the ship 
        #that will result in all the packages on the 
        #conveyor belt being shipped within days days.
        def required_days(capacity,weights):
            load=0
            day=1
            for num in weights:
                if load+num>capacity:
                    day+=1
                    load=num
                else:
                    load+=num
            return day
            

        l=max(weights)
        r=sum(weights)
        
        while l<=r:
            mid_weight=(l+r)//2
            num_days=required_days(mid_weight,weights)
            if num_days<=days:
                r=mid_weight-1
            else:
                l=mid_weight+1
        return l

        