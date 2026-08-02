class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()

        def dfs(start, remaining, path):
            if remaining == 0:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):
                num = candidates[i]

                if num > remaining:
                    break
                
                if i>start and candidates[i] == candidates[i-1]:
                    continue
                
                path.append(num)
                dfs(i+1, remaining - num , path)
                path.pop()


        dfs(0, target, [])
        return res

'''
    🔍 Line-by-Line Explanation (Focus on the New Parts)
    1. The Outer Shell & Sorting
python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort() 

Same as before, but here sorting is NOT optional.

Why? Because we need identical numbers to be right next to each other in the list so we can easily spot and skip them.

    2. The dfs Function (Same start, but stricter rules)
python
def dfs(start: int, remaining: int, path: List[int]):

start: Prevents permutations (stops [1,2] and [2,1]).
remaining: Tracks how much we have left to hit the target.
path: Our current combination.

3. The "Save" Base Case (Unchanged)
python
if remaining == 0:
    res.append(path[:])
    return

Exactly the same as LC 39. If we hit 0, we save a copy.

    4. The Loop & Pruning (Unchanged)
python
for i in range(start, len(candidates)):
    num = candidates[i]
    
    if num > remaining:
        break

Same pruning trick. Since we sorted, if num overshoots, everything after it overshoots too. break out.

    5. CHANGE #1: The Duplicate Skips (The "Danger Zone")
python
if i > start and candidates[i] == candidates[i-1]:
    continue

This is the single most important line in this problem. Let's decode it:

i > start: This ensures we are not looking at the very first element of this current recursion level.

Why? The first element at any level is allowed to be a duplicate (e.g., the first 1 in [1,1,2] must be tried). We only skip the second, third, etc., copies at the same depth.

candidates[i] == candidates[i-1]: If the current number is exactly the same as the previous number in the sorted list, we skip it.

Why continue and not break? Because we are skipping a duplicate, but there might be a larger, valid number later (e.g., skip 1, but 2 is still valid). In LC 39 we used break because we were overshooting. Here we use continue because we are just avoiding repetition.

    6. CHOOSE (Unchanged)
python
path.append(num)
Add the number to the basket.

    7. CHANGE #2: The Recursive Call (The "No Reuse" Rule)
python
dfs(i + 1, remaining - num, path)

THIS IS THE MAJOR CHANGE FROM LC 39.
We pass i + 1 instead of i.

Why? Because in this problem, you cannot reuse the same element. The next recursive call must start at the very next index.

    8. UNCHOOSE (Unchanged)
python
path.pop()
Remove the number to try the next option in the loop.

    9. The Ignition
python
dfs(0, target, [])
return res
Start the recursion.

    📈 Step-by-Step Execution Trace (The "Aha!" Visual)
Let's run this with candidates = [1, 1, 2], target = 3.

(Notice the two 1s are at index 0 and index 1)
Start: dfs(0, 3, [])
Loop i=0 (num=1). i > start? (0 > 0 = False). So we DON'T skip.
Choose [1]. Call dfs(1, 2, [1]).
Inside dfs(1, 2, [1]): (Start index is now 1)
Loop i=1 (num=1). i > start? (1 > 1 = False). We DON'T skip.
Choose [1,1]. Call dfs(2, 1, [1,1]).
dfs(2,1, [1,1]): Loop i=2 (num=2). 2 > 1 → break. Return.
Pop → back to [1].

Loop i=2 (num=2). i > start? (2 > 1 = True). Check candidates[2] ==
candidates[1]? (2 == 1? False). So proceed.
Choose [1,2]. Call dfs(3, 0, [1,2]).
remaining == 0 → ✅ SAVE [1,2] to res. Return.

Pop → back to [1].
Loop ends. Return to root.
Back to Root dfs(0,3,[]):

Loop i=1 (num=1). THIS IS THE TRICKY PART!
i > start? (1 > 0 = True). Check candidates[1] == candidates[0]? (1 == 1 = True).
continue → We SKIP this entirely!

We do NOT start a new branch with this second 1, because [1,2] was already found using the first 1.
Root Loop i=2 (num=2):
Choose [2]. Call dfs(3, 1, [2]) → 2 > 1 breaks. Return.
Final Output: [[1,2]] ✅ (No duplicate [1,2]!)

🧠 Ultimate Revision Cheat Sheet (LC 39 vs LC 40)
Feature	                        LC 39 (Combination Sum)	    LC 40 (Combination Sum II)
Can I reuse the same element?	Yes! Pass i	                No! Pass i + 1
Does input have duplicates?	    No	                        Yes
Need to skip duplicates?	    No                      	Yes! if i > start and candidates[i] == candidates[i-1]: continue
Sorting required?	            No (but good for pruning)	YES! (Required for skipping duplicates)
Overshoot handling	            break	                    break (still works because sorted)

🎯 The Golden Rule for All Variations
Reuse allowed? → Use i.
No reuse? → Use i + 1.
Has duplicates in input? → Add the duplicate-skip if statement.
No duplicates in input? → Skip that if statement.
'''