'''
Explore how to determine the minimum characters to append to a source string to make a target string its subsequence. Learn to apply two-pointer techniques efficiently for solving linear string problems while understanding subsequence concepts and constraints.
Statement
You’re given two strings, source and target, made up of lowercase English letters. Your task is to determine the minimum number of characters that must be appended to the end of the source so that the target becomes a subsequence of the resulting string.

Note: A subsequence is formed by deleting zero or more characters from a string without changing the order of the remaining characters.
'''
def appendCharacters(source, target):
    
    # Replace the following placeholder return statement with your code
    i=0
    j=0
    while i < len(source) and j< len(target):
        if source[i] == target[j]:
            j+=1
        i+=1
    return len(target)-j

'''
Append Characters to String to Make Subsequence

Core Idea:
Find how much of target is already a subsequence of source.

Use Two Pointers:
i -> source
j -> target

If chars match:
    move both pointers

Else:
    move source pointer only

At end:
j = number of target chars matched

Remaining chars:
len(target) - j

These characters must be appended.

Time Complexity: O(n + m)
Space Complexity: O(1)

Pattern:
Subsequence Matching using Two Pointers.
'''