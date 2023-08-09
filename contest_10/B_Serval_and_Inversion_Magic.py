def solve(n,s):
    # Split the string into two halves
    s1, s2 = s[:n//2], s[n//2 if n % 2 == 0 else n//2 + 1:][::-1]
    # Count the number of 0s and 1s in each half
    c1 = s1.count('0')
    c2 = s2.count('0')
    # Check if the number of 0s in s1 is equal to the number of 1s in s2 and vice versa
    if c1 == len(s2) - c2 and c2 == len(s1) - c1:
        print('Yes')
    else:
        print('No')
    


t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    solve(n,s)