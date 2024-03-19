t= int(input())
for _ in range(t):
    n = int(input())
    a = list(map(str,input().split('1')))
    
    print(a)
    long = 0
    for num in a:
        long = max(len(num),long)

    print(long)