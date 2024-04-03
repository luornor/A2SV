class Solution:
    def dailyTemperatures(self, arr: List[int]) -> List[int]:
        n = len(arr)
        stack = []

        res = [0] * n
        for i in range(n):

            while stack and arr[stack[-1]] < arr[i]:
                idx = stack.pop()
                res[idx] = i - idx

            stack.append(i)


        return res