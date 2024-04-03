def solve():
    time = input()
    hour,mins = time.split(":")

    h = int(hour)
    ans= ''
    if h<12:
        if h==0:
            ans = "12:"+ mins + " " + 'AM'
        else:
            ans =  time + " " + "AM"
    else:
        h%=12
        if h==0:
            ans= time + ' '+ "PM"
        else:
            if h<10:
                h = "0"+ str(h)
            ans =  str(h)+":" + mins + " "+ "PM"

    return ans

t = int(input())
for _ in range(t):
    print(solve())
    