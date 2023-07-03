t = int(input())

def solve(l,n):
    # Problem A: 
    # 1: Count the number of occurances of each number in the array
    # 2: Check if the count of number x is less than or equals to the count of (x-1) for all unique x in the array
    
    
    l = sorted(l,reverse=True)

    if n==1 and l[0] != 0:
        return 'NO'
    
    for i in range(n-1):
        r = l[i] #take the first element
        if r==-1:
            continue
        for j in range(i+1,n):
            if l[j]==r-1: #compare max-1 to the next element
                l[j] = -1 #if they are equal mark the element
                r-=1 #then reduce the max_element
            if r==0: #break if max==0
                break
        if r!=0:
            #if the inner loop finishes check if
            #the sequence is correct
            return 'NO'
        
    return 'YES'
        
        
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    print(solve(l,n))
       
