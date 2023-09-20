def solve(a, n):
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]
    
    min_thickness = n  
    
    for first_segment_length in range(1, n + 1):
        current_thickness = first_segment_length
        remaining_sum = first_segment_length
        for i in range(first_segment_length + 1, n + 1):
            if prefix_sum[i] == prefix_sum[remaining_sum] + prefix_sum[first_segment_length]:
                current_thickness = max(current_thickness, i-remaining_sum)
                remaining_sum = i
        if remaining_sum==n:
            min_thickness = min(min_thickness, current_thickness)
    
    print(min_thickness)


t = int(input())
for _ in range(t):
    n =int(input())
    a = list(map(int, input().split()))
    solve(a,n)