
def interpret(command: str) -> str:
    dict = {
        'G':'G',
        '()':'o',
        '(al)':'al',
    }
    interpreted = []
    i = 0
    while i< len(command):
        if command[i]=='G':
            interpreted.append(dict[command[i]])
            i+=1
        elif command[i:i+2]=='()':
            interpreted.append(dict[command[i:i+2]])
            i+=2
        elif command[i:i+4]=='(al)':
            interpreted.append(dict[command[i:i+4]])
            i+=4

    print(''.join(interpreted))
    

    

interpret(input())
        