n = int(input())
s = input()

count = {0:-1}
current = 0

max_len = 0
for i in range(n):

    if s[i]=='0':
        current+=1
    else:
        current-=1

    if current in count:
        max_len = max(max_len, i - count[current])
    else:
        count[current] = i

    # print(count)


print(max_len)
        
        