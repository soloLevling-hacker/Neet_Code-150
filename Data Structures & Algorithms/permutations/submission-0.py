class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def backtrack(start):
            if start == len(nums):
                res.append(nums.copy())
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        
        backtrack(0)
        return res

'''
    1. The Approach (Step-by-Step)
The core idea is: "Fix one position, figure out the rest."

The Pointer (start): This marks the boundary. Everything before start is fixed in the final permutation. Everything from start to the end is available to be placed at start.

The Loop (for i in range(start, len(nums))): We iterate through all available candidates to place at nums[start].

The "Choose" (Swap): nums[start], nums[i] = nums[i], nums[start]. We bring nums[i] into the start position. Now the prefix (up to start) is finalized.

The "Explore" (Recurse): backtrack(start + 1). We move the pointer right to fill the next position.

The "Unchoose" (Swap Back): nums[start], nums[i] = nums[i], nums[start]. We restore the list to exactly how it was before the "choose" step. This ensures that when the loop moves to the next i, the list is back to its original state, keeping the algorithm clean.

    Visual Example (nums = [1, 2, 3]):
start=0, swap (0,0) → [1,2,3], recurse → generates [1,2,3] and [1,3,2].
Backtrack swaps (0,0) back (does nothing).
start=0, swap (0,1) → [2,1,3], recurse → generates [2,1,3] and [2,3,1].
Backtrack swaps (0,1) back → restores to [1,2,3].
start=0, swap (0,2) → [3,2,1], recurse → generates [3,2,1] and [3,1,2].

    2. Why .copy() is Absolutely Required
You might be thinking: "Why can't I just do res.append(nums)?"

    The Dangers of res.append(nums) (No Copy):
Everything is a Reference: In Python, lists are mutable objects passed by reference. If you append nums directly, you are appending a pointer to the actual nums list in memory, not the values inside it.

The Backtracking Wipes It Out: Immediately after you hit the base case and append, the function returns to the previous call and executes the "Unchoose" swap. This physically mutates the original nums list.

The Catastrophic Result: By the time the algorithm finishes, nums has been swapped back to its original state ([1,2,3]). Because you stored pointers, res will look like [[1,2,3], [1,2,3], [1,2,3], ...]—six identical lists, or worse, all references to the exact same object.

    The Solution (res.append(nums.copy())):
.copy() (or nums[:] or list(nums)) creates a brand new, independent list in memory containing the current values at that specific millisecond.

It freezes the snapshot. Even when nums changes drastically in the next recursive branch, the copy safely stored in res remains perfectly untouched.
'''