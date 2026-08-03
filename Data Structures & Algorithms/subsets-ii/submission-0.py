class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(start, path):

            res.append(path.copy())

            for i in range(start, len(nums)):

                if i>start and nums[i] == nums[i-1]:
                    continue

                path.append(nums[i])

                backtrack(i + 1, path)

                path.pop()

        backtrack(0, [])
        return res

'''
    The solution uses backtracking with a duplicate-skipping mechanism.
Sort nums so duplicates are adjacent, enabling controlled skipping.
Define a recursive function backtrack(start, path) that:

Appends a copy of the current path to the result (this captures every valid subset along the way).

Iterates from start to the end of nums.

Skips duplicates at the same recursion level: if i > start and nums[i] == nums[i-1], we continue — this prevents generating identical subsets from duplicate values.

Otherwise, it includes nums[i], recurses with i+1, and then backtracks by popping.

This generates all unique subsets exactly once, leveraging the sorted order to prune duplicate branches.

    Why .copy() (or [:] / list()) is essential
Without copying, res.append(path) would append a reference to the same mutable path list. As backtracking proceeds, path is modified (pop operations), so all stored references would end up pointing to the final empty (or last) state, ruining the result.

Using a copy (.copy(), path[:], or list(path)) saves the current snapshot of the subset. Since we only store integers (immutable), a shallow copy is perfectly sufficient.

All three syntaxes are interchangeable here; choose .copy() for readability, [:] for conciseness, or list() for explicitness — just never store the original mutable object directly.
'''