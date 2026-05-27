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
Lowest Common Ancestor of Binary Tree III

Core Idea:
Use two pointers moving upward using parent pointers.

Pointer Logic:
pointer1 starts from p
pointer2 starts from q

When pointer reaches NULL:
redirect it to other node.

Why This Works:
Both pointers travel:
p-path + q-path

This automatically equalizes depth difference.

Eventually both pointers meet at LCA.

Important Insight:
This problem is similar to:
Intersection of Two Linked Lists

Key Pattern:
Equalizing path lengths using pointer switching.

Time Complexity: O(h)
Space Complexity: O(1)
'''