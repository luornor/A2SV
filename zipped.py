# Enter your code here. Read input from STDIN. Print output to STDOUT
N,X = input().split() #number of students #number of subjects


all_grades = [] 
for _ in range(int(X)):
    grades = list(map(float,input().split()))
    all_grades.append(grades)

grade_sum = 0
for x in list(zip(*all_grades)):
    grade_list = list(x)
    for i in range(len(grade_list)):
        grade_sum+=grade_list[i]
    if int(X)>3:
        print(format(grade_sum/int(X),'.2f'))
    else:
        print(format(grade_sum/int(X),'.1f'))

    grade_sum=0
    
    
    
    

    

    