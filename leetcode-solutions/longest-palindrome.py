from collections import Counter


def longestPalindrome(s):
        # n = len(s)
        # #"abccccdd"
        # #a:1
        # #b:1
        # #c:4
        # #d:2
        
        # Initialize a dictionary to store letter frequencies
        letter_freq = Counter(s)        
        palindrome_length = 0
        odd_frequency_flag = False
        
        # Iterate through the dictionary's values
        for freq in letter_freq.values():
            if freq % 2 == 0:
                palindrome_length += freq
            else:
                palindrome_length += freq - 1
                odd_frequency_flag = True
        
        #Account for an odd frequency character in the center
        if odd_frequency_flag:
            palindrome_length += 1
        
        return palindrome_length