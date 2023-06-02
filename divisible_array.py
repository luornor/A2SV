t = int(input())

def find_greater_num_div_n(x,n):
    """Thi function returns the number that is greater than a number and is divisible by another  """
    q = x//n
    return (q+1)*n

def solve(n):
    ans = [i for i in range(1,n+1)]
    curr_sum = sum(ans)
    next_greater = find_greater_num_div_n(sum(ans),n)
    delta = next_greater-curr_sum
    ans[0]+=delta
    print(*ans)



for _ in range(t):
    #positive integer
    n = int(input())
    solve(n)


