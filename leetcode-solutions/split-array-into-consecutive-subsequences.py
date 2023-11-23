class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        #last element and length
        #sort based on last element
        heap =[]
        for i in range(len(nums)):
            #consecutive
            # print(heap)
            #difference is more than 2
            while heap and (heap[0][0] + 1 < nums[i]):
                    last,length = heappop(heap)
                    if length<3:
                        return False 
            if heap and heap[0][0]+1==nums[i]:
                last,length = heappop(heap)
                last=nums[i]
                length+=1
                heappush(heap,(last,length))
            else:
                heappush(heap,(nums[i],1))
              

        print(heap)      
        while heap:
            last,length = heappop(heap)
            if length<3:
                return False
        return True
    
             

        
                
           