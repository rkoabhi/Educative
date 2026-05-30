def nextPermutation(nums):
    # Write your code here
    n = len(nums)
    pivot = -1
    #first find pivot
    for i in range(n-2,-1,-1):
        
        if nums[i] < nums[i+1]:   # we are comparing i and i+1, so if i i=n-1, then i + 1 would be n, but nums[n] does not exist
            pivot = i
            break
    #found pivot
    if pivot!=-1:
        #find the next larger element
        for i in range(n-1,pivot,-1): # this finds the smallest largest, because it will be in descending
            if nums[i] > nums[pivot]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break
    left = pivot + 1
    right = n - 1
    
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        
        left = left + 1
        right = right -1
                
            
    
    pass



'''
Explore how to rearrange an array to its next lexicographically greater permutation efficiently using the two pointers technique. 
Understand the process to find and implement the next permutation in-place while handling edge cases such as the highest possible order.

Your task is to rearrange an array, nums, containing positive integers to form the next lexicographically greater permutation. 
This means finding the next permutation in the sequence of all possible arrangements sorted in dictionary order.

Step 1
first index from right where
nums[i] < nums[i+1]

Step 2
If pivot exists:
Find smallest larger element from right.
Swap.

Step 3
Reverse suffix.

Edge Case
Suppose I have [3,2,1]
3>2>1
no pivot found, its already the largest
next permutation
[1,2,3], reverse the entire array
Increase the number by the smallest amount possible.

If no pivot exists:
array is descending order.

Example:
[3,2,1]

Next permutation:
[1,2,3]

Time Complexity: O(n)
Space Complexity: O(1)

Pattern:
Find Pivot -> Swap -> Reverse Suffix
'''
