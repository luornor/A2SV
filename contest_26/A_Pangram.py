from collections import Counter


n = int(input())
s = input()
s = s.lower()

letter_count = Counter(s)
if len(letter_count)==26:
    print('YES')
else:
    print('NO')