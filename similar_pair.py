"""
You are given a 0-indexed string array words.

Two strings are similar if they consist of the same characters.

For example, "abca" and "cba" are similar since both consist of characters 'a', 'b', and 'c'.
However, "abacba" and "bcfd" are not similar since they do not consist of the same characters.
Return the number of pairs (i, j) such that 0 <= i < j <= word.length - 1
and the two strings words[i] and words[j] are similar.
There are 2 pairs that satisfy the conditions:
- i = 0 and j = 1 : both words[0] and words[1] only consist of characters 'a' and 'b'. 
- i = 3 and j = 4 : both words[3] and words[4] only consist of characters 'a', 'b', and 'c'. 
"""
def similarPairs(words: list[str]):
        pairs = []
        for i in range(len(words)):
            for j in range(1,len(words)):
                if (0 <= i < j <= len(words)-1) and set(words[i])==set(words[j]):
                     pairs.append((i,j))
 
        return len(pairs)
                  

# words = ["aba","aabb","abcd","bac","aabc"]
# words = ["aabb","ab","ba"]
words = ["nba","cba","dba"]
print(similarPairs(words))