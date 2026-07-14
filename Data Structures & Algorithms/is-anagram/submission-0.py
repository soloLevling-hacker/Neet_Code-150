'''
Approach:
Create a hash map for the first string (s) to count the frequency of each character.
Create another hash map for the second string (t) to count the frequency of each character.
Compare the two hash maps.
If both have the same characters with the same frequencies, the strings are anagrams.
Otherwise, they are not anagrams.
Complexity
Time Complexity: O(n + m) (where n and m are the lengths of s and t)
Space Complexity: O(k) (where k is the number of unique characters)
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        
        for i in s:
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1
        dic2 = {}
        for i in t:
            if i in dic2.keys():
                dic2[i] += 1
            else:
                dic2[i] = 1
        if dic.items() == dic2.items():
            return True           
        else:
            return False
