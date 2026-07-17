'''
1. ch_set = set()
Creates an empty set. This set will store the unique characters that are currently inside our sliding window (left to right). We use a set because lookups (in), additions, and removals are fast (average O(1)).

2. n = len(s)
Stores the length of the input string in a variable for convenience (avoid calling len() repeatedly, though it’s not strictly necessary).

3. left = 0
Initializes the left pointer of our sliding window. It marks the beginning index of the current substring we are examining.

4. max_len = 0
Initializes the variable that will store the length of the longest valid substring found so far. We start at 0 because the string could be empty.

5. for right in range(n):
Starts a loop where right is the right pointer of our sliding window. It iterates through every index in the string, effectively expanding the window one character at a time to the right.

6. while s[right] in ch_set:
Before we can safely add the new character s[right] to our window, we must ensure it doesn't already exist in the set (because a valid substring cannot have duplicates).
If s[right] is already in the set, this while loop runs. It shrinks the window from the left until the duplicate is removed.

7. ch_set.remove(s[left]) (Corrected)
Removes the character located at the current left index from the set. This is how we "kick out" the leftmost character of the window.

8. left += 1
Moves the left pointer one step to the right, effectively shrinking the window size by 1.
(The while loop repeats this process until s[right] is no longer in the set, meaning the window now contains only unique characters).

9. ch_set.add(s[right])
Now that the window guarantees no duplicates of s[right], we add this new character to the set. The window now correctly represents all unique characters from index left to index right.

10. if right - left + 1 > max_len:
Calculates the current window's length (right - left + 1) and checks if it is larger than the maximum length we have recorded so far.

11. max_len = right - left + 1
If the current window is longer, we update max_len to this new value.

12. return max_len
After the loop finishes (we've checked every possible right boundary), we return the overall longest length found.
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch_set = set()
        n = len(s)
        left = 0
        max_len = 0

        for right in range(n):
            while s[right] in ch_set:
                ch_set.remove(s[left])
                left += 1
            ch_set.add(s[right])

            if right - left + 1 > max_len:
                max_len = right - left + 1
        
        return max_len




                