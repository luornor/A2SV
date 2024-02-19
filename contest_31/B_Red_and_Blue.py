from itertools import accumulate


def solve():
    n = int(input())
    reds = list(map(int,input().split()))
    m = int(input())
    blues = list(map(int,input().split()))

    maxx = 0
    red_sum = list(accumulate(reds))
    blue_sum = list(accumulate(blues))

    maxx = max(0,red_sum) + max(0,blue_sum)
    # for i in range(n+1):
    #     for j in range(m+1):
    #         maxx = max(maxx,red_sum[i]+blue_sum[j])

    return maxx


t = int(input())
for _ in range(t):
    print(solve())
    
