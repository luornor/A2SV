def is_subsequence(s1, s2):
    i = 0
    for c in s1:
        if i < len(s2) and s2[i] == c:
            i += 1
    return i == len(s1)

a = input()
b = input()

if a == b:
    print("-1")
else:
    longest_subsequence = max(len(a), len(b))
    if is_subsequence(a, b) or is_subsequence(b, a):
        print(longest_subsequence)
    else:
        print(longest_subsequence)