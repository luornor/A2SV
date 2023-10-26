from bisect import bisect_left
def valid(arr,num):
    idx_sum = 0
    for i in range(len(arr)):
        if arr[i]<num:
            idx_sum+=1

    return idx_sum


def solve(a,n):
    # for i in range(n):
    #     for j in range(i+1,n):
    #         if a[i]<i+1<a[j]<j+1:
    #             count+=1
    count = 0
    valid_indexes = []
    for i in range(n):
        if a[i] < i+1:
            count += valid(valid_indexes,a[i])
            valid_indexes.append(i+1)

    print(count)
# 0 1 3 4 1 2 8 3
# 1 3 5 6 7 8 9 10
# 0 0 1 2 0 1 5 1
# a[i] < i < a[j] < j  
    


    

t = int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    solve(a,n)