'''
    line: res = [1] * n
Creates an output list res of length n, filled with 1s.
Initially: res = [1, 1, 1, 1].
This list will eventually hold the final answers.

    # left products
A comment indicating the first pass: we will compute the product of all elements to the left of each index.

    line: for i in range(1, n):
Starts a loop where i goes from 1 to n-1 (skipping index 0).
Index 0 has no elements to its left, so its left‑product stays 1 (already correct).

    line: res[i] = res[i-1] * nums[i-1]
For index i, we take the previously computed left‑product (res[i-1]) and multiply it by the element just before i in the original array (nums[i-1]).
After this loop, res[i] holds nums[0] * nums[1] * ... * nums[i-1] (the product of every element before i).

Example after left pass for nums = [1,2,3,4]:
i=1: res[1] = res[0] * nums[0] = 1 * 1 = 1
i=2: res[2] = res[1] * nums[1] = 1 * 2 = 2
i=3: res[3] = res[2] * nums[2] = 2 * 3 = 6
Now res = [1, 1, 2, 6].

    # right products multiplied in
Comment for the second pass – we will now multiply each res[i] by the product of all elements to its right.

    line: right = 1
Initializes a variable right to 1. This will store the running product of all elements to the right of the current index as we move from right to left.
For the last element (index n-1), there are no elements to its right, so the right‑product is 1.

    line: for i in range(n-1, -1, -1):
Starts a loop that goes backwards: i starts at n-1 and decreases down to 0 (inclusive). The -1 step means we decrement by 1 each time.

    line: res[i] *= right
Multiplies the current value in res[i] (which currently holds the left‑product) by the running right variable.
At this moment, right holds the product of all elements to the right of i (because we built it up from the previous iterations).
The result is: left_product * right_product = product of everything except nums[i].


    line: right *= nums[i]
After updating res[i], we update right for the next iteration (which will be index i-1).
We multiply the current right by nums[i], so that when we move leftwards, the running product now includes the element we just passed.

Example after right pass for nums = [1,2,3,4] (starting from res = [1,1,2,6]):
i=3: res[3] = 6 * 1 = 6; right = 1 * 4 = 4
i=2: res[2] = 2 * 4 = 8; right = 4 * 3 = 12
i=1: res[1] = 1 * 12 = 12; right = 12 * 2 = 24
i=0: res[0] = 1 * 24 = 24; right = 24 * 1 = 24
Final res = [24, 12, 8, 6] – exactly correct.

Time Complexity: O(n)
First pass (left products): Loop runs n-1 times (from index 1 to n-1).
→ O(n)
Second pass (right products): Loop runs n times (from index n-1 down to 0).
→ O(n)
Total: O(n) + O(n) = O(2n) → simplified to O(n)

Space Complexity: O(1) (excluding output)
res array: O(n) – this is the output array, which is required by the problem and not counted as extra space in most analyses.
Auxiliary space (extra variables):
n → O(1)
right → O(1)
Loop counters → O(1)
Total extra space: O(1) (constant)
'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]
        
        right = 1
        for i in range(n-1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res