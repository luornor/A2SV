def solve(n,k,h):

    ps = [0] * (n + 1)
    for i in range(1, n + 1):
        ps[i] = h[i - 1] + ps[i - 1]
    max_index = 0
    min_sum=ps[k]
    current_sum = min_sum
    r=1
    while r<n-k+1:
        current_sum = current_sum - h[r - 1] + h[r + k - 1]

        if current_sum < min_sum:
            min_sum = current_sum
            max_index = r
        r+=1
    return max_index+1

n, k = map(int, input().split())
h = list(map(int, input().split()))
print(solve(n,k,h))
