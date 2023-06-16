"""Given a string array words, return an array of all characters that show up in all strings
within the words (including duplicates). You may return the answer in any order.
 """

def commonChars(words: list[str]) -> list[str]:
        res = []
        letter_count = {}
        for word in words:
            for char in word:
                  if char in letter_count:
                        

                
        
                       

print(commonChars(["bella","label","roller"]))