if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        students.append([name,score])

    def sort_list(list,index):
        list.sort(key=lambda x:x[index])
        return list
    
    students = sort_list(students,1)
    min_score_name = min(students, key=lambda x:x[1])

    runners_up = []

    for i in range(len(students)):
        if min_score_name[1]<students[i][1]:
            runners_up.append(students[i])

    min_runner_up = min(runners_up, key=lambda x:x[1])
    min_sort = sort_list(runners_up,0)
    for item in runners_up:
        if item[1]==min_runner_up[1]:
            print(item[0])

    

    
    
    

    
        
