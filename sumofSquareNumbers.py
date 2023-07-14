from math import sqrt


def judgeSquareSum(c):
    l = 0
    r = int(sqrt(c)) #4
    while l<=r:
        squared_sum = l**2 + r**2
        if squared_sum==c:
            return True
        elif squared_sum>c:
            r-=1
        else:
            l+=1
    
    return False 
