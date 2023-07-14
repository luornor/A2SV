"""Vasya claims that he had a paper square.
 He cut it into two rectangular parts using one vertical or horizontal cut. 
Then Vasya informed you the dimensions of these two rectangular parts.
 You need to check whether Vasya originally had a square. 
In other words, check if it is possible to make a square using two given rectangles."""

num_points = int(input())

def solve(a1,b1,a2,b2):
    if (a1+a2==max(b1,b2) and b1==b2) or (a1+b2==max(a2,b1) and a2==b1) or (a2+b1==max(a1,b2)and a1==b2)or(b1+b2==max(a1,a2) and a1==a2):
       print('yes')
    else:
        print('no')
        
       


for _ in range(num_points):
    a1,b1 = map(int,input().split())
    a2,b2= map(int,input().split())
    solve(a1,b1,a2,b2)