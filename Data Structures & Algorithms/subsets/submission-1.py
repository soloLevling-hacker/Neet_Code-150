class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(start, path):
            res.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])

                dfs(i+1, path)
                path.pop()
        dfs(0,[])
        return res

'''

Concept	                    Why it’s used
Recursion	                The function calls itself to explore all combinations.
Backtracking	            After exploring one choice, we undo it (path.pop()) to try the next.
DFS (Depth‑First Search)	The recursion explores one branch completely before moving to the next.
Base case	                There is no explicit base case – the loop naturally ends when start == len(nums).
List slicing / copying	    path[:] creates a shallow copy so that later modifications to path don't affect the saved subset.
Passing by reference	    In Python, lists are mutable. We must copy before storing, otherwise all stored subsets would change.
Index management	        start ensures we only pick elements after the current one, avoiding permutations/duplicates.


1. The Core Philosophy: "Pick the Next Item"
Instead of asking "Should I include nums[0]? Should I include nums[1]?" (which is another valid approach), this approach asks: "What is the very next element I am allowed to add?"

Because order doesn't matter in subsets ([1,2] is the same as [2,1]), we enforce a strict rule: We only move forward through the list. We never look back.

2. The Master Key: The start Pointer
This is the most important variable in your code.
At dfs(start, path), the start variable tells you: "You are only allowed to pick elements from index start to the end."
When you pick nums[i], you call dfs(i + 1, ...).
Why i+1? Because you just used index i, so the next element must come after it. 

This guarantees:
You get [1,2] but never [2,1] (because 1 is before 2).
You never reuse the same element twice (no [1,1]).

3. The 3-Step Ritual of Backtracking (The "Move" Pattern)
Inside the for loop, you do exactly three things. Memorize this rhythm:
Choose (Append) – Put the next item into your current basket (path).
Explore (Recurse) – With this new basket, call dfs to find all bigger subsets.
Unchoose (Pop) – Take the item out of the basket so you can try the next item in the for loop.
If you forget Step 3, your path will grow forever and ruin the next iteration.

4. The "Snapshot" Moment (Why we copy)
Notice we add path[:] to res at the very top of the function, before the loop.

This is intentional:
When you first enter dfs, no matter what, the current path is a valid subset.
We immediately take a photo (copy) of it and save it.
Then, we try to grow it bigger by adding more elements in the loop.

5. Visual Walkthrough for nums = [1, 2] (Follow the arrows)
Start: dfs(0, []) → Save []
Loop i=0 (Pick 1): path = [1]
Go inside: dfs(1, [1]) → Save [1]
Loop i=1 (Pick 2): path = [1,2]
Go inside: dfs(2, [1,2]) → Save [1,2]
Loop ends (start=2, out of bounds).
Pop 2 → path = [1] (Back to explore more at level 2, but loop ends)
Pop 1 → path = [] (Back to root)
Loop i=1 (Pick 2): path = [2]
Go inside: dfs(2, [2]) → Save [2]
Pop 2 → path = []
Final Answer: [[], [1], [1,2], [2]]

6. Quick Mental Checklist for Revision
When you see this problem again, run through this checklist in your head:

Goal: Generate combinations of all lengths.

Constraint: No duplicates, order doesn't matter. → Solution: Use a start index.

What to save?: Everything! → Solution: Save a copy at the top of DFS.

How to move?: Pick an index, go deeper (i+1), then pop to clean up.

7. The "Human" Analogy (If it helps)
Imagine you are at a buffet line with plates [1, 2, 3].
You must walk forward (never go back to an earlier dish).
You stand at dish 0. You can either:

Skip it (just go to i+1 without adding it) — but wait! In your specific code, skipping is handled automatically by the for loop moving to the next i.

Take it (append it to your plate), sit down to write down your current plate, then stand up, walk forward, and decide if you want more.

That "sit down to write down your plate" happens at the top of dfs before you pick more food!

Final takeaway for your revision notes:
"This is a 'Generate by Next Choice' backtracking algorithm. The start index prevents permutations. The path[:] captures the current state. The pop resets the state for the next sibling branch."
'''