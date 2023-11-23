def solve(n,m,s,A,B,a_vals,b_vals):
    #sort to ensure we pick vaues of larger values first
    a_vals.sort(reverse=True)
    b_vals.sort(reverse=True)
    #use prefix sum to accumulate values of items
    ps_a = [0]*(n+1)
    ps_b = [0]*(m+1)

    for i in range(1,n+1):
        ps_a[i]=a_vals[i-1]+ps_a[i-1]

    for i in range(1,m+1):
        ps_b[i]=b_vals[i-1]+ps_b[i-1]

    #anytime we pick a value of size A we look for a value of size B that can fit into the bag 
    max_cost = 0
   
    for i in range(n+1):
        rem_weight = (s-i*A)
        if rem_weight<0:
            break
        #how many items of weight B can we take
        num_B = min(rem_weight//B,m)
        max_cost = max(max_cost,ps_a[i]+ps_b[num_B])

    return max_cost



n,m,s,A,B = map(int,input().split())
a_values=list(map(int,input().split()))
b_values = list(map(int,input().split()))


print(solve(n,m,s,A,B,a_values,b_values))