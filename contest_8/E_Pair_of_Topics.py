def solve(n,a,b):
    
    differences = [(a[i]-b[i],i)for i in range(n)]

    differences.sort()
    l,r = 0,n-1 
    good_pair = 0
    while l<r:
        #ai+aj>bi+bj
        if differences[l][0]+ differences[r][0]>0:
            good_pair+=r-l
            r-=1
        else:
            l+=1

        
    print(good_pair)


n = int(input())

teacher_topics = list(map(int, input().split()))
student_topics = list(map(int,input().split()))
solve(n,teacher_topics,student_topics)