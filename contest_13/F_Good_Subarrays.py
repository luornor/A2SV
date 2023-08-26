def solve(a,n):
    #1 2 0
    count = 0
    prefix_sum = [0] * (n + 1)
    prefix_sum[1] = a[0]
    for i in range(1, n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]
    occurrences = {}
    for i in range(n + 1):
        diff = prefix_sum[i] - i
        count += occurrences.get(diff, 0)
        occurrences[diff] = occurrences.get(diff, 0) + 1
    print(count)
        
            

t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    arr = [int(x) for x in a]
    solve(arr,n)