
def interpret(command: str) -> str:
    dict = {
        'G':'G',
        '()':'o',
        '(al)':'al',
    }
    res = ''
    for item in command:
        if item in dict.keys():
            res = ''.join(dict[item])
    print(res)

interpret(input())
        