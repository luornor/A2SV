# n, m, k = map(int, input().split())
# a = list(map(int, input().split()))
# operations = []

# for _ in range(m):
#     li, ri, di = map(int, input().split())
#     operations.append((li, ri, di))

# result = a.copy()

# for _ in range(k):
#     x, y = map(int, input().split())
#     x -= 1 
#     for i in range(x, y):
#         l, r, d = operations[i]
#         for j in range(l - 1, r):
#             result[j] += d

# print(*result)




n, m, k = map(int, input().split())
a = list(map(int, input().split()))
operations = []

for _ in range(m):
    l, r, d = map(int, input().split())
    operations.append((l, r, d))

# Initialize the result array
result = [0] * n

# Calculate prefix sum for operations
ps = [0] * (m + 1)

for i in range(k):
    x, y = map(int, input().split())
    x -= 1  
    # y -= 1
    ps[x] += 1  # Increment the start of the range
    ps[y] -= 1  # Decrement one past the end of the range

#actual values for each operation using prefix sum
for i in range(1, m):
    ps[i] += ps[i - 1]
# print(ps)

# Apply queries and calculate the final result array
for i in range(m):
    l, r, d = operations[i]
    result[l - 1] += ps[i] * d
    if r< n:
        result[r] -= ps[i] * d

# Calculate the cumulative sum for the final result
for i in range(1, n):
    result[i] += result[i - 1]
# print(result)
#Add initial_array to the result to get the final values
for i in range(n):
    result[i] += a[i]

print(*result)
