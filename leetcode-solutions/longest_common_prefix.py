def longestCommonPrefix(str_list):
    #  find the minimum length string from the array
    ans = ''
    min_length = len(str_list[0])
    for i in range(1,len(str_list)):
        if len(str_list[i])< min_length:
            min_length = len(str_list[i])
    
    # loop for the minimum length
    for i in range(0,min_length):
        # get current character from first string
        current = str_list[0][i]
        # check if this character is found in all other strings
        for item in str_list:
            if item[i]!=current:
                return ans
        ans+=current
    return ans
            

strs = ["flower","flow","flight"]
result = longestCommonPrefix(strs)
print(result)