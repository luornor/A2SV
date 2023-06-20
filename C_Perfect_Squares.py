import math
n = int(input())

def solve(a):
    max_num = float('-inf')
    for num in a:
        # negative numbers are not perfect squares taking the floor of the sqrt satifies the condition
        if num < 0 or math.floor(math.sqrt(num))**2 !=num:
            if num> max_num:
                max_num=num
    print(max_num)

a = list(map(int,input().split()))

solve(a)