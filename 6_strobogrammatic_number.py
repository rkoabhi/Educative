'''
Explore how to use the two-pointer approach to determine if a given number is strobogrammatic, meaning it appears the same when rotated 180 degrees. This lesson helps you apply logical steps to verify these numbers in strings while practicing efficient problem-solving strategies.
Statement
Given a string num representing an integer, determine whether it is a strobogrammatic number. Return TRUE if the number is strobogrammatic or FALSE if it is not.

Note: A strobogrammatic number appears the same when rotated 
180
180
 degrees (viewed upside down). For example, “69” is strobogrammatic because it looks the same when flipped upside down, while “962” is not.

 '''

 def is_strobogrammatic(num):
    rotation_list = {
        '0':'0',
        '1':'1',
        '6':'9',
        '8':'8',
        '9':'6'
    }
    left = 0
    right = len(num)-1
    
    while left <=right:
        if num[left] not in rotation_list:
            return False
        if rotation_list[num[left]]!= num[right]:
            return False
        
        left = left +1
        right = right -1

    return True

'''
Strobogrammatic Number

Valid rotations:
0 <-> 0
1 <-> 1
8 <-> 8
6 <-> 9
9 <-> 6

Core Idea:
Use two pointers.

For every pair:
rotation[left_digit] must equal right_digit.

If any digit is invalid or mapping fails:
return False.

Use:
while left <= right

because middle digit of odd-length number
must also be checked.

Middle digit can only be:
0, 1, 8

Time Complexity: O(n)
Space Complexity: O(1)

Pattern:
Palindrome-style two pointer traversal with custom matching rules.
'''