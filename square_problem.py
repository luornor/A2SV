"""Vasya claims that he had a paper square.
 He cut it into two rectangular parts using one vertical or horizontal cut. 
Then Vasya informed you the dimensions of these two rectangular parts.
 You need to check whether Vasya originally had a square. 
In other words, check if it is possible to make a square using two given rectangles."""

num_points = int(input())

def solve(p1,p2):
   
    i = 0
    while i<len(p1)-1:
        if p1[i]*p1[i+1] == 2*(p2[i]*p2[i+1]) or 2*(p1[i]*p1[i+1]) == p2[i]*p2[i+1]:
            print('yes')
        else:
            print('no')
        i+=1
           
        
       


for _ in range(num_points):
    rec1 = list(map(int,input().split()))
    rec2= list(map(int,input().split()))
    solve(rec1,rec2)