n = int(input())
bars = list(map(int, input().split()))

l = 0
r = n - 1
alice_time = 0
bob_time = 0
while l <= r:
    if alice_time <= bob_time:
        l += 1
        alice_time+=bars[l]
    else:
        r -= 1
        bob_time += bars[r]

 

print(*[l, n-l])