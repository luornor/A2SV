n = int(input())

for i in range(n+1):
    for j in range(n+1-i):
        print(' ')
    for j in range(i):
        print(i+1,end='')
    for j in range(-1,n-i-1,-1):
        print(i)
    print()