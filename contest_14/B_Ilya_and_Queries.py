
s = input()
n = len(s)
m = int(input())
queries = [list(map(int, input().split())) for _ in range(m)]

count = [0] * n
#'......'
for i in range(1, n):
    if s[i] == s[i - 1]:
        count[i] = 1
# print(count)
ps = []
p_sum = 0
for num in count:
    p_sum+=num
    ps.append(p_sum)
# print(ps)
for l, r in queries:
    answer = ps[r - 1] - ps[l - 1]
    print(answer)
