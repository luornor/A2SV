def solve():
    n = int(input())
    s = input()

    count = 0
    for i in range(n):
        plus = 0
        minus = 0
        for j in range(i,n):
            if s[j]=='+':
                plus+=1
            else:
                minus+=1
                
            if minus>=plus and (plus-minus)%3==0:
                count+=1
    return count


for _ in range(int(input())):
    print(solve())