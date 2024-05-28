import math

n, k = map(int, input().split())

powers_of_two = []
current_power = 2 ** math.floor(math.log2(n))

while n > 0 and k > 0:
    if n >= current_power:
        n -= current_power
        powers_of_two.append(current_power)
        k -= 1
    else:
        current_power //= 2

if k > 0 or n > 0:
    print("NO")
else:
    print("YES")
    print(*powers_of_two)