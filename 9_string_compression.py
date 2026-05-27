'''
Explore how to apply the two pointers technique to compress strings directly within the input array. Learn to identify groups of repeating characters and represent counts efficiently, including multi-digit lengths. This lesson helps you master an in-place algorithm that uses constant extra space and returns the new length of the compressed array.
Statement
Given an array of characters, chars, compress it in place according to the following rules:

Start with an empty string s.

For each group of consecutive repeating characters in chars:

If the group length is 
1
1
, append just the character to s.

Otherwise, append the character followed by the group length.

The compressed string s should not be returned separately; instead, it must be written directly into the input character array chars. Note that if a group’s length is 
10
10
 or greater, each digit of the length should be stored as a separate character in chars.

After modifying the array, return the new length of the compressed array.

Note: Your solution must use only constant extra space. Any characters beyond the returned length in chars can be ignored.
'''
def compress(chars):
    
    # Replace this placeholder return statement with your code
    read = 0 # to scan groups
    write = 0 # to write compressed output
    while read < len(chars):
        current = chars[read]
        count = 0
        
        while read < len(chars) and chars[read]==current:
            count = count + 1
            read= read + 1
            
        chars[write]=current
        write = write+1
        
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write = write + 1
    
    return write

    '''
String Compression

Pointers:
read  -> scans groups
write -> writes compressed result

Steps:
1. Count consecutive characters
2. Write character
3. If count > 1:
      write count digits
4. Move to next group

Example:
aaabbccc

a3b2c3

Important:
count >= 10

12 -> '1','2'

Use:
for digit in str(count)

Time Complexity: O(n)
Space Complexity: O(1)

Pattern:
Read Pointer + Write Pointer
'''