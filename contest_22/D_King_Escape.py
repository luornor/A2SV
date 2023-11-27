def solve():
    n = int(input())
    q_r,q_c = map(int, input().split())
    k_r,k_c = map(int,input().split())
    target_r,target_c = map(int,input().split())

    #determine range of king with repsect to queen
    R = n if q_r < k_r else 1
    C = n if q_c < k_c else 1

    #if target is in kings range
    if min(R, q_r) <= target_r <= max(R, q_r) and min(C, q_c) <= target_c <= max(C, q_c):
        return 'YES'
    else:
        return 'NO'


print(solve())