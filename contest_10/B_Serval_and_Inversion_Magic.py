def solve(n,s):
    if s == s[::-1]:
        return "Yes"

    illegal_positions = []
    for i in range(1, n // 2 + 1):
        if s[i - 1] != s[n - i]:
            illegal_positions.append(i)

    if len(illegal_positions) <= 1:
        return "Yes"

    if illegal_positions[-1] - illegal_positions[0] == len(illegal_positions) - 1:
        return "Yes"

    return "No"
    

    #Tutorial
    # l = 0
    # r = n
    # while l < r and s[l] == s[r - 1]:
    #     l += 1
    #     r -= 1
    # if l >= r:
    #     print("Yes")
    #     return
    # while l < r and s[l] != s[r - 1]:
    #     l += 1
    #     r -= 1
    # while l < r and s[l] == s[r - 1]:
    #     l += 1
    #     r -= 1
    # if l >= r:
    #     print("Yes")
    # else:
    #     print("No")


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    print(solve(n,s))