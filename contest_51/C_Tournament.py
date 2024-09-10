def solve(n, k, produce):
    dp_full = [0] * n
    dp_half = [0] * n
    
    # Initialize for the first tree
    dp_full[0] = produce[0] - k
    dp_half[0] = produce[0] // 2
    
    for i in range(1, n):
        # Full pick option for tree i
        dp_full[i] = max(dp_full[i-1], dp_half[i-1]) + (produce[i] - k)
        
        # Half pick option for tree i
        half_pick = produce[i] // 2
        dp_half[i] = max(dp_full[i-1], dp_half[i-1]) + half_pick
    
    # The result for this test case is the max of both options for the last tree
    return max(dp_full[n-1], dp_half[n-1])


for _ in range(int(input())):
    n, k = map(int, input().strip().split())
    produce = list(map(int, input().strip().split()))
    
    print(solve(n, k, produce))
    


