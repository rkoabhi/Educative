'''
Explore how to verify if a given string can become a valid palindrome by removing at most one character. This lesson teaches you to apply the two-pointer technique to solve the problem efficiently, with linear time complexity and constant space. By practicing this approach, you'll enhance your skills in handling string and linear data structure problems relevant for coding interviews.
Statement
Write a function that takes a string as input and checks whether it can be a valid palindrome by removing at most one character from it.

'''


def is_palindrome(string):
  def check_pal(left, right):
    while left < right:
      if string[left]!=string[right]:
        return False
      left+=1
      right-=1
    return True
  left = 0
  right = len(string) - 1
  
  while left < right:
    if string[left] == string[right]:
      left+=1
      right-=1
    else:
      return(
        check_pal(left+1,right)
        or
        check_pal(left,right-1)
        )
  return True

  
'''
Valid Palindrome II — Two Pointer Approach

Core Idea:
Palindrome means:
left char == right char

Use:
left pointer
right pointer

Normal Case:
If chars match:
move inward

Mismatch Case:
We are allowed ONE deletion.

So only 2 possibilities:
1. Skip left character
2. Skip right character

Check if either remaining substring is palindrome.

Key Insight:
At first mismatch,
only one of the two chars can be removed.

Helper Function:
is_palindrome(left, right)

Time Complexity: O(n)
Space Complexity: O(1)

'''