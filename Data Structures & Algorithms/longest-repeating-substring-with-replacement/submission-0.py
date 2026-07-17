
'''
Step 1: Initialize the frequency tracker
Create an array freq of size 26 (for uppercase English letters). This will store the count of each character inside our current sliding window.

Step 2: Set up the sliding window pointers
left = 0 (start of the window)
answer = 0 (to store the maximum valid window length found so far)

Step 3: Start expanding the right side
Loop through the string with a right pointer from 0 to len(s) - 1.
This means we are trying to add s[right] into our current window.

Step 4: Add the new character to the frequency map
Take s[right], convert it to an index (e.g., ord(char) - ord('A')), and increment freq[index] by 1.
Now the window officially includes this character.

Step 5: Find the most frequent character in the current window
Calculate max_freq = max(freq).
This tells us the highest count of any single letter inside the window.
(Note: Doing max(freq) costs O(26) per step, which is effectively O(1) since 26 is constant.)

Step 6: Calculate the current window size
window_len = right - left + 1

Step 7: Check if the window is valid
Evaluate if window_len - max_freq > k:.
If this is true, it means we would need to replace more than k characters to make every character in this window identical.
Therefore, the window is invalid, and we must shrink it from the left.

Step 8: Shrink the window (only when invalid)
Take the character at the left pointer: s[left].
Decrement its count in freq because it is leaving the window.
Move the left pointer one step to the right: left += 1.
(Important: We use a while loop for this step in code, but since we only move left by 1 each time and re-check the condition, it's correct. Some optimized versions move left once per loop iteration and re-run the check.)

Step 9: Update the maximum length found so far
After ensuring the current window is valid (either it was valid from the start, or we shrunk it until it became valid), calculate its current length:
current_len = right - left + 1.
Update answer = max(answer, current_len).

Step 10: Move to the next iteration
Increment right and repeat from Step 4. The window will expand again with the next character.

Step 11: Return the final result
After the loop finishes (i.e., right has gone through the entire string), return answer. This is the length of the longest substring we can transform.
'''

'''
Note:-
1.ord(s[left])
ord() is a Python built-in function
It returns the Unicode/ASCII integer value of a character

Examples:
ord('A') = 65
ord('B') = 66
ord('Z') = 90
So if s[left] = 'B', then ord('B') = 66

2.A = ord('A')
This is a constant we defined earlier (outside this line)
ord('A') = 65
So A = 65

3.ord(s[left]) - A
This subtracts 65 from the ASCII value
This maps characters to array indices 0-25:
'A' → 65 - 65 = 0
'B' → 66 - 65 = 1
'C' → 67 - 65 = 2
...
'Z' → 90 - 65 = 25
Why do this? Because our freq array has size 26 (one slot for each letter), and arrays only accept integer indices, not characters.
'''



class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq = [0] * 26
        answer = 0
        left = 0
        A = ord('A')
        n = len(s)

        for right in range(n):
            freq[ord(s[right]) - A] += 1

            max_freq = max(freq)

            length = right - left+1

            if length - max_freq > k:
                freq[ord(s[left]) - A] -= 1
                left +=1

            answer = max(answer, right - left+1)

        return answer
