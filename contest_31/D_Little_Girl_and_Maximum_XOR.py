l,r = map(int,input().split())

# maxx = 0
# for i in range(l,r+1):
#     for j in range(i+1,r+1):
#         maxx = max(maxx,i^j)

# print(maxx)
xor = l ^ r
n = xor.bit_length()

# print(xor)
# print(bit_len)

a = r>>(n) << n


x = a+(2**n)

y = a + ((2**n)-1 )
print(a)
print(x,y)

max_xor = (1<<n) - 1

print(max_xor)

