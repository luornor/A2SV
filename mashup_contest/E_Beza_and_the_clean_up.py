# def max_value(n,s,A,a):
#     a.sort(reverse=True)
#     weight=0
#     cost=0
#     l=0
#     r=0
#     while r<n:
#         weight+=A
#         cost+=a[r]
#         r+=1
#         while weight>s:
#             weight-=A
#             cost-=a[l]
#             l+=1

    
#     return cost


n,m,s,A,B= map(int,input().split())

a=list(map(int,input().split()))
b=list(map(int,input().split()))

def max_total_value(n, m, s, A, B, a, b):
  # Sort the items in descending order of value.
  a.sort(reverse=True)
  b.sort(reverse=True)

  # Initialize the current weight of the trash bag.
  current_weight = 0

  # Iterate over the items in descending order of value.
  for i in range(n):
    if current_weight + A <= s:
      # Add the item to the trash bag.
      current_weight += A
    else:
      break

  for j in range(m):
    if current_weight + B <= s:
      # Add the item to the trash bag.
      current_weight += B
    else:
      break

  # Return the total value of the items in the trash bag.
  return sum(a[0:i]) + sum(b[0:j])



max_total_value = max_total_value(n, m, s, A, B, a, b)

print(max_total_value)




   


