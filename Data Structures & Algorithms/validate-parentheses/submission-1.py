'''
def isValid(s: str) -> bool:
This defines a function. You give it a string s (like "()[]{}"), and it gives you back True (valid) or False (invalid).

    stack = []
This creates our empty "plate tray". In programming, we use a Python list as a stack.
stack.append() will put something on top. stack.pop() will take the top thing off.

    mapping = {')': '(', '}': '{', ']': '['}
This is a cheat-sheet (dictionary).
It says: "If I see a closing ), it must match an opening (."
Notice the keys are only closing brackets, and the values are their matching opening brackets.

    for ch in s:
We look at every single character (ch) in the string s, one by one, from left to right.

        if ch in mapping:  # closing bracket
mapping only contains closing brackets as keys (), }, ]).
So this line asks: "Is this character a closing bracket?"
If YES (it is ) or } or ]), we go inside the if block.

            if not stack or stack.pop() != mapping[ch]:
This is the most important line! It does two checks:

if not stack: Is our tray empty? If we see a closing bracket but there is nothing in the stack, that means we have nothing to close it with! Example: "}". This is instantly invalid, so we return False.
If the tray is not empty, we do stack.pop(). This removes the top plate (the most recent opening bracket) from the stack and hands it to us. We compare it to mapping[ch].
Example: If ch is ], then mapping[ch] is [.
If the popped bracket is not [, that means the brackets don't match (like ( vs ]), so we return False.

        else:              # opening bracket
            stack.append(ch)
If the character was NOT a closing bracket, then it must be an opening bracket ((, {, or [).
We simply put it onto the top of our stack (tray) to remember it for later.

    return not stack
After we finish looking at every character, we check the tray.

not stack means: "Is the stack empty?"
If the stack is empty, it means every opening bracket we put in got popped out by its matching closing bracket. So it's valid (True).
If the stack is not empty, it means we have leftover opening brackets that never got closed (like "(()"). So it's invalid (False).

Let's Walk Through an Example!
Example 1: s = "([)]" (This is invalid)
Step	Character ch	Is it closing?	Action	  Stack (top is on the right)
1	         (	              No	    Push (	  [ '(', ]
2	         [	              No	    Push [	  [ '(', '[' ]
3	         )	              Yes	    Pop       top: '['.
Does '[' match ')'? The cheat-sheet says ) needs (.
'[' != '(' ❌	RETURN FALSE
It fails immediately because [ was closed with ) instead of ].

Example 2: s = "()[]" (This is valid)
Step	Character ch	Is it closing?	Action	  Stack
1	         (	              No	    Push (	  [ '(' ]
2	         )	              Yes	    Pop       top: '('      
Matches ')'? ✅ Yes.	[ ] (empty)

3	         [	              No	    Push [	  [ '[' ]
4	         ]	              Yes	    Pop       top: '['.
Matches ']'? ✅ Yes.	[ ] (empty)

Loop ends. Stack is empty [].
return not stack → not [] is True ✅.
'''



class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for ch in s:
            if ch in mapping:
                if not stack or stack.pop() != mapping[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack
