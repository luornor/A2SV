def swap_case(s):
    s_x  = ''
    for i in s:
        if i.isupper():
            i = i.lower()
        else:
            i = i.upper()
        s_x+=i


    return s_x
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
