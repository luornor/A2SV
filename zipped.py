# Enter your code here. Read input from STDIN. Print output to STDOUT
N,X = input().split() #number of students #number of subjects


all_grades = [] 
for _ in range(int(X)):
    grades = list(map(float, input().split()))
    all_grades.append(grades)

num = 0
index = 0
avg_scores = []
for i in range(int(N)):
    if index==len(all_grades[i]):
        break
    num+=all_grades[i][index]
    avg_scores.append(num/int(X))
    index+=1
    
print(all_grades)
for num in avg_scores:
    print(num)
    
    
    
    

    

    