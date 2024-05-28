s = input()
check = input()
k = int(input())

# s,p=raw_input(),raw_input()
# s=sorted(s[i:] for i in range(len(s)))
# k,x,d=input(),0,ord('a')
# l=''
# for e in s:
#   i,j,y,n=0,0,0,min(len(l),len(e))
#   while i<n and l[i]==e[i]:i+=1
#   n=len(e)
#   while j<n:
#     y+='0'==p[ord(e[j])-d]
#     if y>k:
#       break
#     j+=1
#   x+=max(0,j-i)
#   l=e
# print x

s = input()
alpha = input()
k = int(input())
subs = sorted(s[i:] for i in range(len(s)))
prev = ''
ans = 0
for j in subs:
    uni = False
    bad = 0
    for i in range(len(j)):
        if i >= len(prev) or prev[i] != j[i]:
            uni = True
        if alpha[ord(j[i])-ord('a')] == '0':
            bad += 1
        if bad > k:
            break
        if uni:
            ans += 1
    prev = j
    
print(ans)
   	  	   			      		 			 	 			  	   				 	 	 	 			  		