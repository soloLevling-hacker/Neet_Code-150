'''
Approach:
1.	Use a hash set (set) to store the numbers seen so far.
2.	Traverse the array once.
3.	If the current number is already in the set, a duplicate exists, so return True.
4.	Otherwise, add the number to the set.
5.	If no duplicate is found after traversing the entire array, return False.
'''
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    


