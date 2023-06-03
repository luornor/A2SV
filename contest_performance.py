N = int(input())

def solve(x):
    flag = 0
    num = 0
    n = [int(x[i]) for i in range(len(x))]
    max_score = n[1]
    for i in range(2,len(n)):
        if n[i]>max_score:
            flag=1
            max_score = n[i]
        
        if flag==1:
            num+=1

            
    print(num)
    


x = input().split() 
solve(x)