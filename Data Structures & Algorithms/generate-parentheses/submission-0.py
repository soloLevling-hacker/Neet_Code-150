'''
    IMPORTANT NOTES:
    1. Strings are Immutable (Unchangeable)
When you create a string in Python, it is locked in memory forever. You cannot change a single character inside it.

    Look at how we build the string:
backtrack(s + '(', open_count + 1, close_count)

When the code runs s + '(', it does not add a parenthesis to the end of the old s. Instead, Python:
Reads the old s value.
Reads '('.
Allocates a brand new block of memory.
Copies the old string + the new character into that new block.
Passes that new string to the next recursive call.
The old s that existed in the current function call remains completely unchanged.

    2. We Never Use pop() or del
In some backtracking solutions (especially for generating permutations or subsets), programmers use a list to build the result:

# Alternative approach using a list (MUTABLE)
def backtrack(path):
    if len(path) == 2*n:
        res.append(''.join(path))  # MUST copy here! 
        return
    path.append('(')   # Modifies the list in place
    backtrack(path)
    path.pop()         # Removes it (backtracking)

In that list version, because the list is mutable, you are literally changing the same list object over and over. If you appended the list directly without copying, you would append the same list object multiple times, and it would end up empty at the end! So they must do res.append(path.copy()) or res.append(''.join(path)).

But in your code, we are using strings and the + operator. Because s + '(' creates a new object, the variable s in the current function frame is never mutated.

    3. What happens inside memory?
When we finally hit res.append(s):
s points to a specific string object in memory, e.g., "((()))".
We save that reference into the res list.
The recursion returns to the previous frame. The previous frame still has its own s (e.g., "((()").
The recursion might go on to create a new string "((())".
The old "((()))" object we saved earlier is completely safe—it is immutable and never changes, so we don't need a copy.

    Summary:
Data Type	         Are we mutating it?	        Do we need to copy?
List (mutable)	     Yes(using append/pop)	        YES, must copy before appending, otherwise it changes later.
String (immutable)	 No(using + creates new ones)	NO, because the old string will never change.
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(s,open, close):

            if len(s) == 2 * n:
                res.append(s)
                return

            if open<n:
                backtrack(s + '(', open+1, close)

            if close<open:
                backtrack(s+')', open, close+1)

        backtrack('',0,0)
        return res

'''
    1. The Core Strategy: Backtracking (DFS + Pruning)
Instead of generating every possible combination of ( and ) (which would be 2^2n strings) and then checking if they are valid, we prune invalid paths immediately.

We treat the problem like a binary decision tree:
At each step, we decide whether to add ( or ).
We stop exploring a path the moment it becomes invalid.

    2. The State
To know if a path is valid, our recursive function tracks three things:
s → The current string built so far.
open → Count of ( used.
close → Count of ) used.

    3. The Two Rules (Transitions)
We only allow two moves, strictly enforced:

Move	Condition	    Why?
Add (	open < n	    We haven't used all available left parentheses yet.
Add )	close < open	We must not have more ) than ( at any prefix. This guarantees we never start with ) or make ()).

Crucial insight: If we follow these two rules always, the final string is mathematically guaranteed to be well-formed. We don't need a separate validation step at the end.

    4. The Base Case (Stopping)
When len(s) == 2 * n, we know:
open == n (we used all left brackets).
close == n (we used all right brackets, enforced by the rules).
At this point, we append s to the result and backtrack.

    5. Why it’s called "Backtracking"
Because we use Depth-First Search (DFS):
We go as deep as possible (filling the entire string).
When we hit the base case, we save the result and return (backtrack).

The function automatically reverts to the previous state (since strings are immutable, no explicit undo is needed), and tries the other possible move.

Visual Representation of the Approach (for n=2)
text
                        ""
                       /  
                     "("
                   /      \
                "(("       "()"
               /           /   \
             "(()"       "()("  
             /           /     \
           "(())"     "()()"   (stop, can't add ')')
We explore left (() first, then right ()).

'''
'''
Alternative Approaches (For completeness)
Brute Force (Naive)

Generate all 
2
2
n
2 
2n
  strings using recursion.

Check each with a balance counter (open == close and never negative).

Time: 
O(n^2)→ Terrible for n=8+.

Dynamic Programming (Closure Number)
The insight: Any valid string can be split as (A)B where A and B are valid parentheses strings of smaller sizes.
Build results for n=0 up to n.

Time: 
O(4n/n)
(similar to Catalan, but iterative).
Complexity: A bit harder to code cleanly in an interview.

BFS (Queue)
Same logic as DFS, but uses a queue to build strings level-by-level. It works, but DFS is more memory-efficient for the call stack.

Why the Backtracking Approach is the Best
Clean & Intuitive: Easier to explain in 5 minutes.
Optimal: It generates exactly the Catalan number of strings 
 C n
and never wastes time building invalid prefixes.

Space: Only uses 
O(n)
O(n) recursion stack (plus the output list).
'''