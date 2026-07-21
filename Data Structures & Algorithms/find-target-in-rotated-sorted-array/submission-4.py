"""
In a rotated sorted array, if you pick the middle element (mid), at least one half (either the left half or the right half) is guaranteed to be perfectly sorted in ascending order.
We use that guarantee to decide exactly where to look for the target.

The Decision Tree (Step-by-Step):
Imagine you have left, right, and mid. Here is exactly what your brain should do:
Check the middle: If nums[mid] == target, you won! Return mid.
Figure out which half is perfectly sorted:

Case A: Left half is sorted.
How to check? if nums[left] <= nums[mid] (No rotation break happened between left and mid).
Can we find the target here? Check if target is between nums[left] and nums[mid] (inclusive of left, exclusive of mid).
Yes? Throw away the right half. (right = mid - 1)
No? Throw away the left half. (left = mid + 1)

Case B: Left half is NOT sorted.
That means the rotation break is on the left, so the right half MUST be perfectly sorted.
Can we find the target here? Check if target is between nums[mid] and nums[right] (exclusive of mid, inclusive of right).
Yes? Throw away the left half. (left = mid + 1)
No? Throw away the right half. (right = mid - 1)

complexity:
time: O(log n)
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
