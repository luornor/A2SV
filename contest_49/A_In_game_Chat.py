for _ in range(int(input())):
    n = int(input())
    s = input()
    list_s = list(s)
    count = 0
    for i in range(n-1, -1, -1):
        if list_s[i] != ')':
            break
        count+=1

    if count > n-count:
        print('Yes')
    else:
        print('No')
