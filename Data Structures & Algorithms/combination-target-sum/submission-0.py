class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(start, remaining, path):
            if remaining == 0:
                res.append(path[:])
                return
            
            for i in range(start, len(nums)):

                num = nums[i]
                
                if num > remaining:
                    break
                
                path.append(num)
                dfs(i, remaining - num, path)
                path.pop()

        dfs(0, target, [])
        return res

'''

    🔍 Line-by-Line Explanation
    1. The Outer Shell
python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

This is just LeetCode's required format.
candidates = the list of numbers you can pick from.
target = the number we want our combinations to sum to.

    2. The Result Bucket
python
res = []

res will hold all our valid combinations (lists of integers).

At the end, we return this.

    3. The Secret Weapon: Sorting
python
candidates.sort() 

We sort the list smallest to largest (e.g., [2,3,6,7]).

Why? It doesn't change the answer, but it allows us to use a pruning trick.

If the current number is already bigger than what we have left (remaining), we know every number after it is also bigger, so we can safely break out of the loop and save time.

    4. The Heart: The dfs Function
python
def dfs(start: int, remaining: int, path: List[int]):

start: The index in candidates where we are allowed to start picking. (Prevents duplicates like [2,3] and [3,2]).

remaining: How much more sum we need to hit the target. We start with target, and subtract as we pick numbers.

path: Our current list of picked numbers (our "plate" from the buffet analogy).

    5. The "Found It!" Base Case
python
if remaining == 0:
    res.append(path[:])
    return

When do we save? When remaining hits exactly 0, it means the numbers in path add up perfectly to the original target.

Why path[:]? We take a copy of path. If we just appended path directly, it would change later when we add/remove numbers. A copy freezes the moment.

return stops this branch because we don't need to add more numbers (it would go negative).

    6. The Looping & Pruning
python
for i in range(start, len(candidates)):
    num = candidates[i]
    
    if num > remaining:
        break

We loop from start to the end.
num is the current candidate we are thinking about adding.

The Genius Pruning Trick: Since the list is sorted, if num is greater than what we have left (remaining), adding it would overshoot the target. Because all numbers after num are even bigger, we can break out of the loop entirely. We don't need to check them.

    7. The 3-Step Backtracking Ritual (The Magic)
python
path.append(num)                     # 1. CHOOSE
dfs(i, remaining - num, path)        # 2. EXPLORE
path.pop()                           # 3. UNCHOOSE

Step 1 (Choose): Put num into our current path.

Step 2 (Explore):
Call dfs to find combinations using this new state.
CRITICAL: We pass i, NOT i+1.
Why? Because we are allowed to reuse num unlimited times. Passing i means the next recursive call can start at the same index and pick num again (e.g., [2,2]).
We pass remaining - num because we just used up that much of our target.

Step 3 (Unchoose): Remove num from path so we can try the next number in the for loop (e.g., try 3 after we are done trying all combinations starting with 2).

    8. The Ignition & The Finish
python
dfs(0, target, [])
return res
We kick off the recursion starting at index 0, with the full target, and an empty path.

After the recursion explores every single possibility, we return the filled res.

    📈 Step-by-Step Execution Trace (for [2,3,6,7], target 7)
Let's see the path variable change over time:

dfs(0, 7, []) → loop at i=0 (num=2).

Append 2 → [2]. Call dfs(0, 5, [2]).

dfs(0, 5, [2]) → loop at i=0 (num=2).

Append 2 → [2,2]. Call dfs(0, 3, [2,2]).

dfs(0, 3, [2,2]) → loop at i=0 (num=2).

2 is not > 3. Append 2 → [2,2,2]. Call dfs(0, 1, [2,2,2]).

dfs(0,1, ...) loops: num=2. 2 > 1, so break. Return.

path.pop() → back to [2,2]. Loop moves to i=1 (num=3).

3 is not > 3. Append 3 → [2,2,3]. Call dfs(1, 0, [2,2,3]).

remaining == 0 → SAVE [2,2,3] to res. Return.

path.pop() → back to [2,2]. Loop continues to i=2 (num=6). 6 > 3, so break.

Return.

path.pop() → back to [2]. Loop in dfs(0,5, [2]) moves to i=1 (num=3).

Append 3 → [2,3]. Call dfs(1, 2, [2,3]).

dfs(1,2, ...) loops from 1: num=3. 3 > 2, so break. Return.

path.pop() → back to [2]. Loop continues... eventually tries 6, 7, but they overshoot.

path.pop() → back to []. Root loop moves to i=1 (num=3), i=2 (num=6), i=3 (num=7).

Eventually, when num=7, append 7 → [7]. Call dfs(3, 0, [7]) → SAVE [7].

Final Output: [[2,2,3], [7]] ✅

    💡 The "Aha!" Moments to Remember
i vs i+1: This single character is the entire difference between "use once" and "use infinite times".

break vs continue: We use break because we sorted the list. If 2 overshoots, 3 definitely will too.

No visited set needed: The start pointer handles all the ordering, so we never get duplicates like [3,2,2].

You now have the complete mental blueprint. Try writing it out on paper without looking—if you nail the i and the remaining == 0 check, you've got it 100%! 🚀
'''