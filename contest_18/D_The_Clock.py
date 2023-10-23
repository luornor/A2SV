def format(hour,minute):
    if hour<10:
        hour = '0'+ str(hour)
    if minute<10:
        minute= '0'+str(minute)
    return f"{hour}:{minute}"

def solve(clock,x):
    # time,k = clock.split()
    hour,mins = clock.split(':')
    
    #change mins into hours and modularize mins
    check_hours = int(x)//60
    check_mins = int(x)%60
    hour = int(hour)
    mins = int(mins)
    count = 0
    while True:
        #count minutes before hours
        mins+= check_mins
        if mins>=60:
            mins = mins%60
            hour+=1

        hour+=check_hours
        if hour>=24:
            hour = hour%24
        
        
        curr_time = format(hour,mins)
        if curr_time[::-1]==curr_time:
            count+=1

        if curr_time==clock:
            break

    print(count)  


        



t = int(input())

for _ in range(t):
    clock,x=input().split()
    solve(clock,x)
