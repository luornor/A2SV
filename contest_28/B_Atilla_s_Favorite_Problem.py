def solve():
    n = int(input())
    s = input()
    max_ = max(s)
    size = ord(max_)-ord('a')
    return size+1



t = int(input())
for _ in range(t):
    print(solve())