'''
Explore how to determine if an abbreviation correctly represents a given word by applying the two pointers technique. This lesson helps you handle numeric skips and letter matches, ensuring full coverage without leading zeros or missing characters.
Statement
A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their respective lengths. The numeric replacements must not contain leading zeros.

Given a string word and an abbreviation abbr, determine whether abbr is a valid abbreviation of word.

The abbreviation abbr consists of lowercase English letters and numeric values. Each numeric value in abbr represents the number of characters skipped in word. Letters in abbr must match the corresponding characters in word exactly. The abbreviation is valid if and only if it fully accounts for every character in word from left to right with no characters remaining or missing.
'''


def valid_word_abbreviation(word, abbr):
    i = 0
    j = 0
    
    while i < len(word) and j < len(abbr):
        
        if abbr[j].isalpha():
            if word[i]!=abbr[j]:
                return False
            i=i+1
            j=j+1
            
        else:
            if abbr[j]=='0':
                return False
                
            num=0
            
            while j<len(abbr) and abbr[j].isdigit():
                num = num * 10 + int(abbr[j])
                j = j+1
            i = i+num
    return i == len(word) and j == len(abbr) 
    