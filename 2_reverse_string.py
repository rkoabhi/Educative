'''
Explore the two pointers technique to reverse the order of words in a string without altering the characters within each word. Learn to manage spaces effectively by removing leading, trailing, and extra spaces, and return a clean, properly spaced sentence.
Statement
You are given a string sentence that may contain leading or trailing spaces, as well as multiple spaces between words. Your task is to reverse the order of the words in the sentence without changing the order of characters within each word. Return the resulting modified sentence as a single string with words separated by a single space, and no leading or trailing spaces.

Note: A word is defined as a continuous sequence of non-space characters. Multiple words separated by single spaces form a valid English sentence. Therefore, ensure there is only a single space between any two words in the returned string, with no leading, trailing, or extra spaces.

Constraints:

The sentence contains English uppercase and lowercase letters, digits, and spaces.

There is at least one word in a sentence.
'''
def reverse_words(sentence):
    
    result = []
    i = len(sentence) - 1
    
    while i>=0:
        
        while i>=0 and sentence[i] == ' ':
            i=i-1
      
            
        if i < 0:
            break
        j=i
        while i>=0 and sentence[i]!=' ':
            i= i-1
            
        result.append(sentence[i+1:j+1])
    return " ".join(result)

'''
Reverse Words in a String — Two Pointer Approach

Core Idea:
Scan string from RIGHT → LEFT.
Why?
Because output word order is reversed.

Pointer Meaning:
i -> moving scanner
j -> end of current word

Algorithm:
1. Skip spaces
2. Mark end of word using j
3. Move i left until space found
4. Extract word using:
   sentence[i+1 : j+1]
5. Add word to result
6. Repeat

Important:
sentence[start:end]
includes start
excludes end

So:
sentence[i+1 : j+1]

Why i+1?
Because i stops at SPACE before word.

Why j+1?
Because slicing excludes ending index.

Example:
sentence = "the sky is blue"

Extracted order:
blue
is
sky
the

Then:
" ".join(result)

join() combines list into single string using spaces.

Example:
["blue", "is", "sky"]

becomes:

"blue is sky"

Key Learning:
This problem is mainly about:
- string parsing
- handling spaces
- extracting substrings using two pointers

Time Complexity: O(n)
Space Complexity: O(n)
'''