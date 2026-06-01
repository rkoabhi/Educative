'''
Understand how to apply the two pointers technique to calculate the minimum number of adjacent swaps needed to make a string palindrome. Practice implementing this approach to solve linear data structure problems efficiently.
Statement
Given a string s, return the minimum number of moves required to transform s into a palindrome. In each move, you can swap any two adjacent characters in s.

Note: The input string is guaranteed to be convertible into a palindrome.

'''

def min_moves_to_make_palindrome(s):
    # Replace this placeholder return statement with your code
    chars = list(s)
    left = 0
    right = len(chars) - 1
    
    moves = 0
    
    while left < right:
        k = right
        
        while k > left and chars[k]!=chars[left]:
            k-=1
        if k == left:
            chars[k], chars[k+1] = chars[k+1], chars[k]
            moves += 1
            
        else:
            while k< right:
                chars[k],chars[k+1]= chars[k+1],chars[k]
                
                moves+=1
                k+=1
            left+=1
            right-=1
    
    return moves

'''
Minimum Adjacent Swaps To Make Palindrome

Two Pointer Idea:

left -> start
right -> end

For each left character:
find matching character from right side.

Case 1:
Match found.
Bubble it to right using adjacent swaps.
Count swaps.
Move both pointers inward.

Case 2:
No match found.
Character must be the middle character.
Swap it one step toward center.
Count one move.
Keep pointers unchanged.

Python:
list(s) -> convert string to mutable list

Adjacent swap:
chars[i], chars[i+1] = chars[i+1], chars[i]

Time Complexity: O(n²)
Space Complexity: O(n)

Pattern:
Two Pointers + Greedy Swapping


while k > left and chars[k] != chars[left]:
    k -= 1

and

while k < right:

    chars[k], chars[k+1] = chars[k+1], chars[k]

    moves += 1
    k += 1


# Example

Suppose:

chars = ['m','a','m','a','d']

Initially:

left = 0
right = 4

m a m a d
L       R


# First While Loop

k = right

while k > left and chars[k] != chars[left]:
    k -= 1

Initially:

k = 4

So:

m a m a d
L       k

## Iteration 1

Check:

k > left

becomes:

4 > 0

True.
Check:

chars[k] != chars[left]

becomes:

'd' != 'm'

True.

Therefore:

k -= 1

Now:

k = 3

m a m a d
L     k


## Iteration 2

Check:

'a' != 'm'

True.

Move:

k = 2

m a m a d
L   k

## Iteration 3

Check:

'm' != 'm'

False.

Loop stops.


# What Did We Just Find?

We searched from RIGHT toward LEFT looking for:

chars[left]

which is:

'm'

Found at:

k = 2

# Now Second While Loop

Current:

m a m a d
    k   R

Need to move this matching:

'm'

to position:

right

using adjacent swaps.

---

Code:

while k < right:

Currently:

2 < 4

True.


# Iteration 1

Swap:

chars[2], chars[3] = chars[3], chars[2]


Before:

```text
m a m a d
```

After:

```text
m a a m d
```

Moves:

```python
1
```

Now:

```python
k = 3
```

Visual:

```text
m a a m d
      k R
```

---

# Iteration 2

Check:

```python
3 < 4
```

True.

Swap:

```python
chars[3], chars[4]
```

Before:

```text
m a a m d
```

After:

```text
m a a d m
```

Moves:

```python
2
```

Now:

```python
k = 4
```

---

Check:

```python
4 < 4
```

False.

Stop.

---

# What Happened?

We "bubbled" the matching:

```python
'm'
```

to the end.

Exactly like bubble sort.

---

# Why Adjacent Swaps?

Problem says:

> You can only swap adjacent characters.

So:

Not allowed:

```python
m a m a d

↓

m a d a m
```

in one move.

---

Allowed:

```python
m a m a d
```

Swap neighbors:

```python
m a a m d
```

1 move

Then:

```python
m a a d m
```

2 moves

---

# Entire Purpose Of The Two Loops

### First Loop

```python
while k > left and chars[k] != chars[left]
```

Meaning:

```text
Search from right side
for a matching character.
```

---

### Second Loop

```python
while k < right
```

Meaning:

```text
Once found,
move it to the right end
using adjacent swaps.
```

---

# Tiny Example

Suppose:

```python
a b c b a
L       R
```

Already:

```python
a == a
```

Search loop immediately finds match.

No swaps needed.

---

Suppose:

```python
a b c a b
L       R
```

Search loop finds:

```python
a
```

at index 3.

Then swap loop moves it:

```python
a b c b a
```

1 move.

---

'''