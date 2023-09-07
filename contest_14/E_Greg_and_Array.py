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
df = [0] * (m + 1)

for i in range(k):
    x, y = map(int, input().split())
    x -= 1  
    df[x] += 1  # Increment the start of the range
    df[y] -= 1  # Decrement one past the end of the range
print(df)
#actual values for each operation using prefix sum
for i in range(1, m):
    df[i] += df[i - 1]

print(*result)
