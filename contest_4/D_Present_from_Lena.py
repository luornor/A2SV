
n = int(input())

# first half of the present

for i in range(n+1):
    t = -1
    for j in range((2*n)+1):
        if (j>=n-i) and (j<=n+i):
            if j<=n:
                t+=1
                print(t,end='')
            else: 
                t-=1
                print(t,end='')
            if j!= n+i:
                print(" ",end='')
        elif j<= n-i:
            print(" ")
    
    

#second half of the present
    










# n = int(input())
# y = 1
# for i in range((2*n)+1):
#     row = [" "] * ((2*n)+1)

#     z = 0
#     while z < y:
#         row[n] = y-1
#         row[n-z] = row[n+z] = y-z-1
#         z+=1
    
#     if i < n:
#         y+=1
#     else:
#         y-=1
    
#     i = 0
#     while i < len(row):
#         if i > n and row[i] == " ":
#             row.pop(i)
#         else:
#             i+=1

#     print(*row)