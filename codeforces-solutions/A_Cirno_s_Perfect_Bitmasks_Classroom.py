def solve():
    x = int(input())
    count = x.bit_count()
    binary_num = bin(x)[2:]
    first_one = binary_num.rfind('1')
    first_zero = binary_num.rfind('0')
    ans = ['0']*(x.bit_length())
    if x==1:
        return 3
    # if count is one find position of first one turn it 1 find first zero turn it to one
    # else find first one  and change it to 1
    if count==1:
        ans[first_one]='1'
        ans[first_zero]='1'
        # print(ans)
        # print(binary_num)

    else:
        ans[first_one]='1'
    
    return int(''.join(ans),2)


    

    

t = int(input())

for _ in range(t):
    print(solve())