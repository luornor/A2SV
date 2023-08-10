def longestConsecutive(nums):
        #[100,4,200,1,3,2]
        #1 2 3 4 100 200
        hset = set(nums)
        longest = 0
        if not nums:
            return longest

        for num in nums:
            #if num-1 not in set it means it is a start
            #of a sequence
            
            if (num-1) not in hset:
                count=1
                while num+count in hset:
                    count+=1
                longest = max(count,longest)
                
        return longest