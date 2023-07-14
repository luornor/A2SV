def solve(n,a):
    count_even = len([num for num in a if num%2==0])
    count_odd = n-count_even
    if count_even > 0 and count_odd > 0:
        a.sort()

    print(*a)

n = int(input())
a = list(map(int, input().split()))

solve(n,a)


# a_original = a.copy()
# def check_lexicograph(x,y):
#     for i in range(len(x)):
#         if x[i] < y[i]:
#             return True
#         elif x[i] > y[i]:
#             return False
#     return True
        

# for i in range(n-1):
#     if (a[i]+a[i+1]) % 2 != 0:
#         a[i],a[i+1] = a[i+1],a[i]
#         break

# if check_lexicograph(a,a_original):            
#     print(*a)


            

   
