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



ps = [0] * (m + 1)

for i in range(k):
    x, y = map(int, input().split())
    x -= 1  
    ps[x] += 1  
    ps[y] -= 1  

#first range update
for i in range(1, m):
    ps[i] += ps[i - 1]
# print(ps)
#second range update
ps2 = [0] * (n+1)
for i in range(m):
    l, r, d = operations[i]
    ps2[l - 1] += ps[i] * d
    ps2[r] -= ps[i] * d
# print(result)
for i in range(1, n):
    ps2[i] += ps2[i - 1]
# print(result)


for i in range(n):
    a[i] += ps2[i]

print(*a)
