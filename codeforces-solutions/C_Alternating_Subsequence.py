
def sign(num):
    return num>=0


def solve(n,nums):
    l,r = 0,0
    arr = []
    #find segments of the same sign
    while r<n:
        while r< n-1 and sign(nums[r])==sign(nums[r+1]):
            r+=1
        arr.append(nums[l:r+1])
        r+=1
        l = r
    #find maximum element in each segment and sum them
    max_sum = 0
    for item in arr:
        if item:
            max_sum+=max(item)

    print(max_sum)
    
    



t = int(input())
    
for _ in range(t):
    n = int(input())
    sequence = list(map(int,input().split()))
    solve(n,sequence)