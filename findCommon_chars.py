"""Given a string array words, return an array of all characters that show up in all strings
within the words (including duplicates). You may return the answer in any order.
 """

def commonChars(words: list[str]) -> list[str]:
        letter_count = {}
        for ch in words[0]:
            if ch in letter_count:
                letter_count[ch]+=1
            else:
                letter_count[ch]=1
        
        for word in words:
            if word==words[0]:
             continue
            check = {}
            for ch in word:
                if ch in letter_count:
                    check[ch] = min(letter_count[ch], check.get(ch, 0) + 1)
                    # hmap[ch]-=1
                    # if ch in check:
                    #     check[ch]+=1
                    # else:
                    #     check[ch]=1     
            letter_count = check
                    
        common_list = [key for key, value in letter_count.items() for _ in range(value)]
        return common_list


                      
                
        
                       

#print(commonChars(["cool","lock","cook"]))
print(commonChars(["bella","label","roller"]))