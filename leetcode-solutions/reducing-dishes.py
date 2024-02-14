class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        satisfaction.sort()

        total_sum = 0

        for i in range(n-1,-1,-1):
            idx = 1
            j=i
            curr_sum = 0
            while j<n:
                curr_sum+=satisfaction[j]*idx                    
                idx+=1
                j+=1
            if curr_sum<total_sum:
                curr_sum=0
            else:
                total_sum=curr_sum

        return total_sum
            