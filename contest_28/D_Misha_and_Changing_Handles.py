
q = int(input())
changed_users = {}
for _ in range(q):
    old, new = input().split()
    # print(changed_users.items())
    if old in changed_users:
        changed_users[new]=changed_users[old]
        del changed_users[old]
    else:
        changed_users[new]=old


print(len(changed_users))

for new,old in changed_users.items():
    print(old,new)
 	 		  	 								 				 	   	