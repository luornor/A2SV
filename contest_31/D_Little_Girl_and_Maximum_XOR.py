l,r = map(int,input().split())

# maxx = 0
# for i in range(l,r+1):
#     for j in range(i+1,r+1):
#         maxx = max(maxx,i^j)

# print(maxx)
xor = l ^ r
bit_len = xor.bit_length()

# print(1<<bit_len)
max_xor = (1 <<bit_len) - 1

print(max_xor)

