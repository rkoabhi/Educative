'''
Understand how to detect a duplicate number in an array where values range from 1 to n using the fast and slow pointer technique. 
Explore the constraints, problem statement, and strategies to solve this challenge efficiently without modifying the original array or using extra space.
Statement
Given an array of positive numbers, nums, such that the values lie in the range 
[1,n]
, inclusive, and that there are n+1
 numbers in the array, find and return the duplicate number present in nums. There is only one repeated number in nums, but it may appear more than once in the array.

'''

def find_duplicate(nums):

    # Replace this placeholder return statement with your code
    slow = nums[0]
    fast = nums[0]
    
    while True:
        
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]
    
    while slow!=fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow

'''
Find Duplicate Number - WHY Floyd Works

1. Treat array as linked list:
   index -> value

2. Duplicate causes two paths to merge.

3. Merge creates a cycle.

Phase 1:
slow = 1 step
fast = 2 steps

They meet somewhere inside cycle.

Reason:
Fast gains 1 step per iteration
and eventually catches slow.

Phase 2:
Reset slow to start.

Move both 1 step.

They meet at cycle entrance.

Important:
Cycle entrance = duplicate number.

Key Insight:
Duplicate value is the point where
multiple paths merge into the cycle.
'''
