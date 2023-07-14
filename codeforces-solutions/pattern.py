"""
In this task, a pattern will be a string consisting of small English letters and question marks ('?'). 
The question mark in the pattern is a metacharacter that denotes an arbitrary small letter of the English alphabet.
We will assume that a string matches the pattern 
if we can transform the string into the pattern by replacing the question marks by the appropriate characters.
For example, string aba matches patterns: ???, ??a, a?a, aba.
you need to find a pattern that contains as few question marks as possible, and intersects with each of the given patterns.
Two patterns intersect if there is a string that matches both the first and the second pattern.
"""
N = int(input())
res = []

def find_intersection_pattern(patterns):
    if not patterns:
        return ""

    intersection_pattern = ""
    pattern_length = len(patterns[0])

    for i in range(pattern_length):
        current_char = patterns[0][i]

        is_question_mark = False

        for pattern in patterns:
            if pattern[i] != current_char:
                if pattern[i] != '?':
                    intersection_pattern += pattern[i]
                    is_question_mark = True
                    break

        if not is_question_mark:
            intersection_pattern += 'x'

    print(intersection_pattern)




        
        
            
res = []
for _ in range(N):
    res.append(input())


find_intersection_pattern(res)




