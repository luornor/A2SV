import ast
def isAlienSorted(words: list[str], order: str) -> bool:
    new_order = [item for item in order if item!='"']
    new_words = ast.literal_eval(words)
    global priorities
    priorities = {letter: index for index, letter in enumerate(new_order)}

    result = sorted(new_words, key=sorting_condition)
    print(result==new_words)

def sorting_condition(word):
    priority_values = []
    #process each word
    for ch in word:
        priority_values.append(priorities[ch])
    
    return tuple(priority_values)

isAlienSorted(input(),input())

