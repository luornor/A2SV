n = int(input())


def print_pattern(n):
    
    odd = 1
    for i in range(n):
        print(' '*(n-i))
        print(i+1)

print_pattern(n)