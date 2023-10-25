class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #If cnt is strictly greater than midmidmid. According to the
        # Pigeonhole Principle, repeated elements are in the 
        #interval [left,mid]
        #Otherwise, the repeated element is in the interval
        # [mid+1,right].
        l = 0
        r = len(nums)-1
        #[1,3,4,2,2]
        fast = 0
        slow = 0
            
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow==fast:
                break

        slow = 0
        while slow!=fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow