def solve(n,claims):
     # Count the number of people who want to go for each ai value
    ai_counts = [0] * n
    for ai in claims:
        ai_counts[ai] += 1
    
    cumulative_count = 0
    not_sad = [False] * n
    
    # Iterate through the claims in decreasing order of ai
    for i in range(n - 1, -1, -1):
        cumulative_count += ai_counts[i]
        if cumulative_count >= i:
            for j in range(i, n):
                not_sad[j] = True
            break
    
    print(not_sad.count(True))



t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    solve(n,a)