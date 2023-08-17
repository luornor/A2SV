
def solve(n,a):
    odd = sorted(a[i] for i in range(n) if a[i] % 2)
    even = sorted(a[i] for i in range(n) if a[i] % 2 == 0)
    odd.sort()
    even.sort()

    sorted_array = []
    even_idx = 0
    odd_idx = 0

    for num in a:
        if num % 2 == 0:
            sorted_array.append(even[even_idx])
            even_idx += 1
        else:
            sorted_array.append(odd[odd_idx])
            odd_idx += 1

    if sorted_array == sorted(a):
        return 'YES'
    else:
        return 'NO'

    


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    print(solve(n,a))