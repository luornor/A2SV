def countWays(ranges):
        mod_val = 1000000007
        ranges.sort()
        previous = ranges[0]
        ans = 0
        n = len(ranges)
        for i in range(1,n):
            prev_end = previous[1]
            curr_start = ranges[i][0]
            if curr_start <= prev_end:
                previous[1] = max(previous[1],ranges[i][1])
            else:
                ans+=1
                previous = ranges[i]
        ans+=1
        return int((pow(2,ans,mod_val)))