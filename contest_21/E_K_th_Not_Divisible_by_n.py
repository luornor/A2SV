def how_many(num,div):
    return num-(num//div)

def solve(n, k):
    #we can't iterate through all the numbers
    quotient = (k-1)//(n-1)
    rem = (k-1)%(n-1)
    return n*(quotient+rem)+1
    # return k + (k-1)//(n-1)   
#     l=1
#     r= 2**31
  
#     while l<=r:
#         mid = (l+r)//2
#         not_div =  how_many(mid,n)

#         if not_div<k:
#             l=mid+1
#         else:
#             r=mid-1

#     return l


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))
