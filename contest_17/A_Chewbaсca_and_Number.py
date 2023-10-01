x = input()
for i in range(len(x)):
    if int(x[i]) > 4:
        x = x[:i] + str(9 - int(x[i])) + x[i+1:]

if x[0] == '0':
    x = '9' + x[1:]

print(x)

