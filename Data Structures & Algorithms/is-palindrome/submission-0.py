'''
Line 1: strs = []
What it does:
Creates an empty list named strs.
This list will act as our "filtered container" – we'll store only the characters we care about.

Why a list?
Lists are mutable (we can add items to them dynamically).
They maintain order (characters are appended in the same order they appear in s).
Later, we'll compare this list to its reverse.

Memory note:
At this point, strs points to an empty list object in memory: []

Line 2: for ch in s:
What it does:
This starts a loop that iterates through the input string s.
ch is the loop variable that takes on the value of each character in s, one by one, from left to right.

Line 3: if ch.isalnum():
What it does:
This is a conditional statement that checks if the current character ch is alphanumeric.
isalnum() is a built-in string method that returns:
True if ch is a letter (A-Z or a-z) OR a digit (0-9)
False if ch is anything else (space, punctuation, special characters like !, @, #, $, etc.)

The logic:
This if statement acts as a filter.
Only if ch.isalnum() returns True do we execute the next line (line 4).
If it returns False, we skip line 4 and move to the next iteration of the loop.

Line 4: strs.append(ch.lower())
What it does:
This line only executes when the if condition is True (i.e., ch is alphanumeric).

It does two things:
ch.lower() – Converts the character to lowercase.
This ensures case-insensitive comparison later.

strs.append(...) – Adds the lowercase character to the end of the strs list.
How append() works:
append() is a list method that adds a single element to the end of the list.
It modifies the list in-place (doesn't create a new list).

Line 5: return strs == strs[::-1]
What it does:
This line checks if the filtered list (strs) is a palindrome.
It does this by comparing strs with its reverse.

Breaking it down:
Part 1: strs[::-1] – The Reverse
This uses Python's slicing syntax: [start : stop : step]
start is omitted → starts from the beginning (index 0)
stop is omitted → goes to the end
step = -1 → moves backwards through the list
The result is a new list that is the reverse of strs

Part 2: strs == strs[::-1] – The Comparison
== checks if the two lists are identical (same elements in the same order).
if there's a mismatch, the result is False.

Part 3: return ...
The function immediately returns the boolean result (True or False).
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for ch in s:
            if ch.isalnum():
                strs.append(ch.lower())
        return strs == strs[::-1]  
