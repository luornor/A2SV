class Solution:
    def splitString(self,s: str) -> bool:
        def backtrack(prev_num,start_idx):
            #base case
            if start_idx == len(s):
                #We've reached the end of the string,
                # which means we found a valid split.
                return True

            # is valid (descending order, difference of 1)
            for i in range(start_idx,len(s)):
                val = int(s[start_idx:i+1])
                #valid (descending order and a difference of 1)
                # Recursively explore the next part of the string
                if prev_num-val==1 and backtrack(val,i+1):
                    return True
            return False

        # Iterate through all possible candidates
        for i in range(len(s)-1):
            substring = s[:i+1]
            #prev_num and next index
            if backtrack(int(substring),i+1):
                return True

        return False

            
             

            

        

        