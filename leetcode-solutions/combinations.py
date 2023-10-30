class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        def is_valid_state(state):
        # check if it is a valid solution
        return True

        def get_candidates(state):
            return []

        def search(state, solutions):
            if is_valid_state(state):
                solutions.append(state.copy())
                # return

        for candidate in get_candidates(state):
            state.add(candidate)
            search(state, solutions)
            state.remove(candidate)

        def solve():
            solutions = []
            state = set()
            search(state, solutions)
            return solutions

        """
        # def is_valid_state(state):
        #     if not state:
        #         return False
        #     if len(state)==k:
        #         return True
            

        # def get_state_candidate(state):
        #     res = []
        #     for arr in state:
        #         for i in range(1,len(arr)):
        #             res.append(i)
        #     return res

        # def search(state,solutions):
        #     if is_valid_state(state):
        #         solutions.append(state.copy())
        #         return
        #     for candidate in get_state_candidate(state):
        #         state.add(candidate)
        #         search(state,solutions)
        #         state.remove(candidate)

        # state = set([1,n])
        # solutions = []
        # search(state,solutions)
        # return solutions
        

        def backtrack(start,stack,n):
            #if find solution add it to result
            if len(stack)==k:
                res.append(stack[:])
                return 
            #iterate over all possible candidates
            for i in range(start,n+1):
                    #try this partial candidate
                    stack.append(i)
                    #given the candidate explore further
                    backtrack(i+1,stack,n)
                    #remove candidate
                    stack.pop()
        res=[]
        stack = []
        backtrack(1,stack,n)
        return res





        
        




                

        