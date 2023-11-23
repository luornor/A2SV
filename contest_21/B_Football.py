def solve(s):
    dangerous = 'NO'

    if s[0] == '0':
        count_0 = 1
    else:
        count_0 = 0

    count_1 = 1 if s[0] == '1' else 0

    for i in range(1, len(s)):
        if s[i] == '1':
            if s[i] == s[i-1]:
                count_1 += 1
            else:
                count_1 = 1
        elif s[i] == '0':
            if s[i] == s[i-1]:
                count_0 += 1
            else:
                count_0 = 1

        if count_1 >= 7 or count_0 >= 7:
            dangerous = 'YES'
            break

    return dangerous


s = input()
print(solve(s))