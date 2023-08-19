
def solve(n):
    if n % 2 == 1:
        return "YES"  # n is odd, so it has an odd divisor greater than 1
    else:
        while n % 2 == 0:
            n //= 2  # Divide n by 2 until it's no longer even
        if n > 1:
            return "YES"  # If n is greater than 1, it means it has an odd divisor
        else:
            return "NO" # If n is 1, it means it only has 1 as a divisor, which is not odd




t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))