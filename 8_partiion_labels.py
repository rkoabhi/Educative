'''
Explore how to apply the two pointers technique to partition a string into as many parts as possible, making sure each character appears in only one part. Understand the problem constraints, practice solution development, and gain skills to solve similar linear data structure challenges efficiently.
Statement
You are given a string s. Your task is to divide the string into as many parts as possible such that each letter appears in at most one part.

In other words, no character should occur in more than one partition. After concatenating all parts in order, the result should be the original string s.

For example, given s = "bcbcdd", a valid partition is ["bcbc", "dd"]. However, partitions like ["bcb", "cdd"] or ["bc", "bc", "dd"] are invalid because some letters appear in multiple parts.

Return a list of integers representing the sizes of these partitions.
'''
def partitionLabels(s):
  
    # Replace this placeholder return statement with your code
    last = {}
    for i,ch in enumerate(s):
        last[ch]=i
    result = []
    start = 0
    end = 0 # farthest future occurence of any chararcter seen so far
    
    for i, ch in enumerate(s):
        end = max(end, last[ch])
        
        if i == end:
            result.append(end - start + 1)
            start = i + 1
    return result

   '''
Partition Labels

Core Idea:
A partition can end only when all characters seen so far
have their last occurrence inside the current partition.

Step 1:
Store last occurrence of every character.

Step 2:
Maintain:
start -> partition start
end   -> farthest last occurrence seen so far

For every character:
end = max(end, last[ch])

When:
i == end

Current partition is complete.

Partition length:
end - start + 1

Then:
start = i + 1

Time Complexity: O(n)
Space Complexity: O(1)

Key Insight:
'end' represents how far the current partition must extend
to include all future occurrences of characters seen so far.
'''