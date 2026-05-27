'''
Explore how to rotate an array by shifting its elements to the right by k positions using the two-pointer approach. Understand problem constraints and implement your solution to strengthen array manipulation skills.
Statement
Given an integer array, nums, shift its elements to the right by k positions. In other words, rotate the array to the right by k steps, where k is non-negative
'''
def rotate(nums, k):
    n=len(nums)
    k = k%n
    
    def reverse(left,right):
        while left < right:
            nums[left], nums[right] = nums [right], nums[left]
            left = left + 1
            right = right - 1
    reverse(0,n-1)
    reverse(0,k-1)
    reverse(k,n-1)
'''
Rotate Array

Core Idea:
Use Reverse-Reverse-Reverse trick.

For rotation by k:

1. Reverse whole array
2. Reverse first k elements
3. Reverse remaining elements

Example:
[1,2,3,4,5,6,7]

Reverse all:
[7,6,5,4,3,2,1]

Reverse first 3:
[5,6,7,4,3,2,1]

Reverse rest:
[5,6,7,1,2,3,4]

Important:
k = k % len(nums)

Used for:
k > array length

Helper:
reverse(left,right)

Uses two pointers:
swap ends and move inward.

Time Complexity: O(n)
Space Complexity: O(1)

Pattern:
Array Reversal + Two Pointers
'''
