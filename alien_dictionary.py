def isAlienSorted(words: list[str], order: str) -> bool:
    
    priorities = {letter: index for index, letter in enumerate(order)}
    # new_words = ' '.join(words)
    result = sorted(words, key=lambda x: tuple(map(lambda y: priorities[y], x)))
    if result == words:
        print(True)
    else:
        print(False)


isAlienSorted(input().split(),input())

# data = ['ayyaaauu', 'shhasyhh', 'shaash']
# ordering = ['s', 'y', 'u', 'h', 'a']
# priorities = {letter: index for index, letter in enumerate(ordering)}

# result = sorted(data, key=lambda x: tuple(map(lambda y: priorities[y], x)))

# # Prints ['shhasyhh', 'shaash', 'ayyaaauu']
# print(result)