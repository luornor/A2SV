def solve(n,arr):
    alice, bob = 0, 0
    l, r = 0, n - 1
    a_sum=arr[l]
    b_sum =arr[r]
    
    while l <= r:
        if a_sum <= b_sum:
            a_sum += arr[l + 1]
            l += 1
            alice += 1
        else:
            b_sum += arr[r - 1]
            r -= 1
            bob += 1
    
    print(alice,bob,end=" ")

n = int(input())
arr = list(map(int, input().split()))

solve(n,arr)
