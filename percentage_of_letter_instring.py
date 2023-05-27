def percentageLetter(s: str, letter: str) -> int:
    count = 0
    num = len(s)
    
    for item in s:
        if letter == item:
            count+=1
    return int((count/num)*100)
    
print(percentageLetter('foobar','o'))