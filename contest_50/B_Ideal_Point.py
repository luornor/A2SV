for _ in range(int(input())):
    n,k = map(int,input().split())
    ideal = False
    left_seg = 0
    right_seg = 0
    for _ in range(n):
        l,r = map(int,input().split())

        if l==k:
            left_seg+=1
        if r==k:
            right_seg+=1
        
        if right_seg>=1 and left_seg>=1:
            ideal=True

    if ideal:
        print('YES')
    else:
        print('NO')




	 				 	 			 	 	 	 	 				 		 		