def solve():
    s = input()
    length = len(s)

    for i in range(length):
        print(s[i], end='')

    for i in range(length - 1, -1, -1):
        print(s[i], end='')

solve()