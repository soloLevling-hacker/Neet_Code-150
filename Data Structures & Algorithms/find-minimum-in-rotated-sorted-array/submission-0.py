'''
Example 1:
Input: nums = [3,4,5,6,1,2]
Output: 1

Example 2:
Input: nums = [4,5,0,1,2,3]
Output: 0

Example 3:
Input: nums = [4,5,6,7]
Output: 4

Exaple_diff:
Input: nums = [3,4,5,6,1,7]
Output = 3
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right =len(nums) - 1

        while left<right:
            mid = (left+right)//2

            if nums[mid]>nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left] 