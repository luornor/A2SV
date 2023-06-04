# Enter your code here. Read input from STDIN. Print output to STDOUT
N,X = input().split() #number of students #number of subjects


grade1 = list(map(float, input().split()))
grade2 = list(map(float, input().split()))
grade3 = list(map(float, input().split()))
    
for i in range(int(N)):
    num_sum = grade1[i]+grade2[i]+grade3[i]
    print(round(num_sum/int(X),1))
    

    

    