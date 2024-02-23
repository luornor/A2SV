def solve():
    x = int(input())
    #count the number of ones
    #if count is greater than one find position of first one and return
    #the number
    #else find first zero and combine with number of first one
    number_of_ones = x.bit_count()
    #find first one
    pos = 0
    while pos<x.bit_length():
        if x & 1<<pos != 0:
            break
        pos+=1

    #find first zero
    zero = 0
    while zero<x.bit_length():
        if x & 1<<zero ==0:
            break
        zero+=1

    if number_of_ones > 1:
        return 2**pos
    else:
        return (1<<pos) ^ (1<<zero)

t = int(input())

for _ in range(t):
    print(solve())