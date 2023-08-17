"""
Let's iterate over the length of the first segment of the split.
Having fixed it, we actually fixed the sum that needs to be collected on all other segments. 
Since each element must belong to exactly one segment, we can build other segments greedily.
If we have found a solution, we will remember the length of the longest segment in it and
try to update the answer. We have n possible lengths of the first segment, 
for each of which we greedily built the answer for n.
Thus, the asymptotics of the solution will be O(n2).
"""
def solve(a, n):
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]
    
    min_thickness = n  # Initialize with maximum possible thickness
    
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