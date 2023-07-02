n = int(input()) #array size

a = list(map(int,input().split()))

start = 0
#find start index
for i in range(n-1):
    if a[i]>a[i+1]:
        start = i
        break

end = 0
for i in range(n-1,0,-1):
    if a[i]<a[i-1]:
        end=i
        break

#reverse the array numbers at start and end
reverse_seg = a[start:end+1][::-1]
# print(start)
# print(end)
# print(reverse_seg+a[end+1:])
# Check if the array is sorted after reversing the segment
sorted_a = a[:start]+ reverse_seg + a[end+1:]
if sorted(a) == sorted_a:
    print('yes')
    print(start+1,end+1)
else:
    print('no')


