
def solve(n,nums):
    maxsum = 0
    neg = 0
    flag = 0
    for i in range(n):
        maxsum+=abs(nums[i])
        if nums[i]<0:
            if neg==0:
                neg=1
                flag+=1
        elif nums[i]>0:
            neg=0

    print(maxsum,flag)


    
          

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    solve(n,arr)