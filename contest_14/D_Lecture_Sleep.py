n, k = map(int, input().split())
a = list(map(int, input().split()))
t = list(map(int, input().split()))

# Calculate prefix sums for theorems
ps = [0] * (n + 1)
for i in range(1, n+1):
    ps[i] = ps[i-1] + a[i-1] * t[i-1]
# Calculate the total theorems when Mishka is awake (without using the technique)
total_awake_theorems = ps[-1]

# Calculate theorems when the technique is used
max_extra_theorems = sum(a[i] if t[i] == 0 else 0 for i in range(k))
extra_theorems = max_extra_theorems
for i in range(k, n):
    extra_theorems = extra_theorems - (a[i-k] if t[i-k] == 0 else 0) + (a[i] if t[i] == 0 else 0)
    max_extra_theorems = max(max_extra_theorems, extra_theorems)

# Maximum theorems is the sum of theorems when Mishka is awake and 
# the maximum extra theorems when the technique is used
max_theorems = total_awake_theorems + max_extra_theorems

print(max_theorems)