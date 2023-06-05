"""Juan loves the Dakti song and wants to memorize the chorus of the song. His friend sent him the chorus in phrases, but the phrases are somewhat strange; they do not have an order and they have numbers. His friend helps Juan organize the chorus of the song.

First, organize the words based on the numbers they have, then delete the numbers once they are organized."""
N = int(input())

def sorting_condition(word):
    #process each input
    num = ''
    for chr in word:
        if chr.isdigit():
            num+=chr
    return int(num)

def remove_numbers(string):
    result = ''
    for chr in string:
        if not chr.isdigit(): #if it is not a digit
            result+=chr
    return result

def solve(n):
    #process each input
    sorted_list = sorted(n,key=sorting_condition)
    organise =' '.join(sorted_list)
    chorus = remove_numbers(organise)
    print(chorus)
    


for _ in range(N):
    n = input().split()
    solve(n)