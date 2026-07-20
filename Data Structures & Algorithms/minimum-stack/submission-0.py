'''
The Analogy: A Stack of "Memo Cards" 🗂️
Instead of just stacking plates, imagine you are stacking memo cards on a desk.

On each card, you write two numbers:
The actual number you are pushing.
The smallest number you've seen so far (including this card).
The brilliant part? You don't need a separate notebook anymore! Because each card remembers the "minimum up to this point." If you remove the top card, the card underneath it instantly tells you what the minimum was before it.

The Code, Line-by-Line
class MinStack:

    def __init__(self):
        self.stack = []  # Each element is [value, current_min]

We create one empty list called self.stack.
The comment is super important: We aren't storing just numbers. We are storing little 2-item lists inside.
Example: self.stack = [ [5, 5], [2, 2], [7, 2] ]

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append([val, val])
        else:
            current_min = min(val, self.stack[-1][1])
            self.stack.append([val, current_min])

This is the heart of the logic:
if not self.stack: Is the stack empty?
If YES, this is the first number ever. The smallest number so far is just val itself. So we push [val, val].
else (There is already stuff in the stack):
We look at the top card on the stack: self.stack[-1].
Remember, each card is a [value, min]. So self.stack[-1][1] grabs the minimum written on that top card.

current_min = min(val, self.stack[-1][1]) → Is the new value smaller than the previous minimum? If yes, update it. If not, keep the old minimum.
We push our new card: [val, current_min].

    def pop(self) -> None:
        self.stack.pop()

We just throw away the top card.
Magic trick: We don't need to recalculate the minimum! Because the new top card already has the correct "minimum up to this point" written on it from when we pushed it earlier.

    def top(self) -> int:
        return self.stack[-1][0]
self.stack[-1] grabs the top card.

[0] grabs the first number written on it (the actual value).
Example: If the top card is [7, 2], this returns 7.

    def getMin(self) -> int:
        return self.stack[-1][1]
self.stack[-1] grabs the top card.

[1] grabs the second number written on it (the minimum so far).
Example: If the top card is [7, 2], this returns 2. Perfect!

Let's Walk Through Your Exact Code in Action!
Let's do: push(-2), push(0), push(-3), getMin(), pop(), getMin()

Step	Code Action	        What the Stack Looks Like	      Explanation
1	    push(-2)	        [ [-2, -2] ]	                  Stack empty, so first card is [-2, -2].
2	    push(0)	            [ [-2, -2], [0, -2] ]	          Previous min was -2. min(0, -2) is -2. So we store [0, -2].
3	    push(-3)	        [ [-2, -2], [0, -2], [-3, -3] ]	  Previous min was -2. min(-3, -2) is -3. Store [-3, -3].
4	    getMin()	                    -	                  Look at top card [-3, -3] and return the second value: -3 ✅
5	    pop()	            [ [-2, -2], [0, -2] ]	          We remove the top card [-3, -3].
6	    getMin()	                    -                     Look at new top card [0, -2]. Return the second value: -2 ✅
Notice how after popping, the new top card already had -2 written on it from Step 2! We didn't have to loop or search.
'''


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append([val,val])
        else:
            current_min = min(val, self.stack[-1][1])
            self.stack.append([val, current_min])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
