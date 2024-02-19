class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        larger = -1
        for i in range(len(arr)-1,-1,-1):
            if arr[i]<arr[i-1]:
                larger=i-1
                break

        smaller = larger+1
        for i in range(larger+1,len(arr)-1):
            if arr[i]<arr[i+1]<arr[larger]:
                smaller = i+1
            
                
        
        # print(larger,smaller)

        if smaller!=-1 and larger!=-1:
            arr[larger],arr[smaller] = arr[smaller],arr[larger] 

        return arr

        

        