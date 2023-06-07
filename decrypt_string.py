"""def split_strings(string):
    numbers = []
    current_number = ""

    for char in string:
        if char != "#":
            current_number += char
        else:
            if current_number:
                numbers.append(current_number + "#")
            current_number = ""

    if current_number:
        numbers.append(current_number)

    return numbers

# Example usage
string1 = "10#11#12"
string2 = "1326#"

result1 = split_strings(string1)
result2 = split_strings(string2)

print(result1)  # Output: ['10#', '11#', '1', '2']
print(result2)  # Output: ['1', '3', '26#']
"""
def freqAlphabets(s: str) -> str:
        s_list = s.split('#')
        print(s_list)
       
                  
        
        alpha_dict = {
                '1':'a',
                '2':'b',
                '3':'c',
                '4':'d',
                '5':'e',
                '6':'f',
                '7':'g',
                '8':'h',
                '9':'i',
                '10#':'j',
                '11#':'k',
                '12#':'l',
                '13#':'m',
                '14#':'n',
                '15#':'o',
                '16#':'p',
                '17#':'q',
                '18#':'r',
                '19#':'s',
                '20#':'t',
                '21#':'u',
                '22#':'v',
                '23#':'w',
                '24#':'x',
                '25#':'y',
                '26#':'z'
        }
        
    
        
                 
                

freqAlphabets(input())