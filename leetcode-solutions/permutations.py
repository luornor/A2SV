class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def is_valid_state(state):
            
            return len(state)==len(nums)
            

        def get_state_candidate(state):
            candidates = []
            for num in nums:
                if num not in state:
                    candidates.append(num)
            return candidates

        def search(state,solutions):
            if is_valid_state(state):
                solutions.append(state.copy())
                return
            for candidate in get_state_candidate(state):
                state.append(candidate)
                search(state,solutions)
                state.remove(candidate)

        state = []
        solutions = []
        search(state,solutions)
        return solutions
        