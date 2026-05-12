'''
Explore how to efficiently sort an array containing red, white, and blue colors represented by 0, 1, and 2 using the two pointers approach. Understand how to implement this one pass algorithm without extra space and apply it to coding interview problems involving linear data structures.
Statement
You are given an array nums of length n, where each element represents an object colored either red, white, or blue. The integers 0, 1, and 2 are used to represent red, white, and blue, respectively.

Sort the array in place so that all objects of the same color are grouped together, arranged in the order: red (0), white (1), and blue (2).

You must solve this problem without using any library sort function.

Note: Could you come up with a one pass algorithm using only constant extra space?

'''



def sort_colors(colors):
    low = 0
    mid = 0
    high = len(colors)-1
    
    while mid <=high:
        if colors[mid] == 0:
            colors[low], colors[mid] = colors[mid], colors[low]
            low = low + 1
            mid = mid + 1
        
        elif colors[mid] ==1:
            mid = mid + 1
            
        elif colors[mid] == 2:
            colors[mid], colors[high] = colors[high], colors[mid]
            high = high - 1
    # Replace this placeholder return statement with your code
    return colors

'''
Sort Colors — Dutch National Flag Algorithm
1.................
CASE 1 → Found 0
nums[mid] == 0
What should happen?

0 belongs LEFT.
So give it to low.
Swap:

nums[low], nums[mid] = nums[mid], nums[low]
Then both move.
Why?
Because:
left side became correct
current index processed

2..............
CASE 2 → Found 1

1 belongs in middle.

Do nothing.

Just move scanner.

mid += 1

3.............

CASE 3 → Found 2

2 belongs RIGHT.

Give it to high.

Swap:

nums[mid], nums[high] = nums[high], nums[mid]

Move high.

BUT NOT mid.
Why NOT Move mid?
Suppose:
[1,2,0]
At:
mid = 1
high = 2
We swap:
[1,0,2]
The new value at mid is:
0
This still needs processing.
If we moved mid, we'd skip it.
'''