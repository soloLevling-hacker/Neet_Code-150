'''
Title: Hash Map + Complement Lookup
approach:
1. Create an empty hash map (dictionary) to store:
        Key: Number
        Value: Index of that number
2. Iterate through the array once.
3. For each element, calculate the complement:
        complement = target - current_number
4. Check if the complement already exists in the hash map.
        Yes: Return the index of the complement and the current index.
        No: Store the current number and its index in the hash map.
5. Continue until the pair is found.

Complexity:
Time: O(n)
Space: O(n)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}

        for i in range(len(nums)):

            complement = target - nums[i]

            if complement in dic:
                return [dic[complement], i]
            
            dic[nums[i]] = i