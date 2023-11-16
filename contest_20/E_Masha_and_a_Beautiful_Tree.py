


def solve(nums):
    count = 0
    def sort(p):
        if len(p)==1:
            return p
        
        mid = len(p)//2
      
        left = sort(p[:mid])
        right = sort(p[mid:])

        res = left + right
        nonlocal count
        if right[-1]<left[-1]:
            res = right + left
            count+=1

        return res
    
    ans = sort(nums)

    if ans==sorted(nums):
        return count
    else:
        return -1
     
    



t = int(input())
for _ in range(t):
    m = int(input())#power of two size of permutation
    nums = list(map(int,input().split()))
    print(solve(nums))
    
    # res= solve(p)
    # if res==sorted(p):
    #     print(count)
    # else:
    #     print(-1)