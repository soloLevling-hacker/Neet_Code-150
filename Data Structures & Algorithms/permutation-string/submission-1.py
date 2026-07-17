"""
1.  if n1 > n2:
        return False
If the pattern is longer than the whole string we're searching, it's impossible to find it. Return False immediately.

2. Creating the "Difference" Array (Lines 7-9)
        diff = [0] * 26
This creates a list of 26 zeros: [0, 0, 0, ..., 0]
Each position represents a letter:
index 0 = 'a'
index 1 = 'b'
...
index 25 = 'z'

What is diff?
It will store:
(how many of this letter we need in s1) – (how many of this letter are currently in our window).

3.  for i in range(n1):
Loop from i = 0 up to (but not including) n1.
In our example, n1 = 2, so this loop runs for i = 0 and i = 1.
This loop sets up the very first window of s2 (the first n1 characters).

4.  diff[ord(s1[i]) - 97] += 1
ord(s1[i]) gives the ASCII number of the character. For 'a', it's 97; for 'b', it's 98.
ord(s1[i]) - 97 turns 'a' → 0, 'b' → 1, etc.
So this line says: "We need one more of this letter from s1" → increase diff by 1.

Example:
i = 0, s1[0] = 'a' → index 0 → diff[0] += 1 → diff[0] becomes 1
i = 1, s1[1] = 'b' → index 1 → diff[1] += 1 → diff[1] becomes 1
Now diff = [1, 1, 0, 0, ...] (we need one 'a' and one 'b').

5.  diff[ord(s2[i]) - 97] -= 1
This looks at the same position i in s2 and decreases diff.
Why? Because our current window already contains this letter, so we subtract it from our "needs".

Example:
i = 0, s2[0] = 'e' → index 4 ('e' is the 5th letter) → diff[4] -= 1 → diff[4] becomes -1
i = 1, s2[1] = 'i' → index 8 → diff[8] -= 1 → diff[8] becomes -1

Now diff has:
diff[0] = 1 (we need one 'a', have 0)
diff[1] = 1 (we need one 'b', have 0)
diff[4] = -1 (we need 0 'e', have 1 → we have extra 'e')
diff[8] = -1 (we need 0 'i', have 1 → extra 'i')

6.  Counting How Many Letters Match (Lines 11-13)
        matches = sum(1 for x in diff if x == 0)

This counts how many positions in diff are exactly 0.
If diff[letter] == 0, it means "we need exactly the same amount as we have" → that letter is balanced.
In our first window ("ei"), the balanced letters are all the ones not mentioned (like 'c', 'd', etc.) because we need 0 and have 0.
'a' has 1 (not balanced), 'b' has 1 (not), 'e' has -1 (not), 'i' has -1 (not).
All other 22 letters have 0, so matches = 22.

7.  if matches == 26:
            return True
If all 26 letters are balanced, then our window is exactly a permutation of s1.

For our example, matches = 22, so we skip this and continue.

8. Sliding the Window (Lines 15-31)
Now we'll slide the window one step at a time across s2.

    for i in range(n1, n2):
range(2, 8) gives us i = 2, 3, 4, 5, 6, 7.
At each step, we add the new character at position i (right side) and remove the old character at position i - n1 (left side).
This moves our window of size n1 from left to right.

9.  Adding the New Character (Right Side)
        idx_in = ord(s2[i]) - 97

Get the index of the new character we're adding to the window.
For i = 2, s2[2] = 'd' → index 3.

10.  if diff[idx_in] == 0:
        matches -= 1
Before we change diff, check if this letter was balanced (diff == 0).
If it was balanced, and we're about to change it, it will become unbalanced, so we decrease matches by 1.

11.  diff[idx_in] -= 1
We are adding this character to our window.
Since diff = (needed) - (window has), if the window has more of this character, the difference goes down by 1.

Example: For 'd', we needed 0, now we have 1 → 0 - 1 = -1.

12.   if diff[idx_in] == 0:
        matches += 1
After changing, check if it's now balanced. If yes, increase matches.

13.  Removing the Old Character (Left Side)
        idx_out = ord(s2[i - n1]) - 97
Which character is leaving the window?
When i = 2, i - n1 = 0, so we remove s2[0] which is 'e' (index 4).

14.     if diff[idx_out] == 0:
            matches -= 1
Same logic: if it was balanced before we change it, it will become unbalanced → decrease matches.

15.    diff[idx_out] += 1
We are removing this character from our window.
The window now has less of this letter, so the difference (needed - window) goes up by 1.

Example: For 'e', we had -1 (needed 0, had 1). After removing it, we have 0 → difference becomes 0.

16.    if diff[idx_out] == 0:
                matches += 1
After the change, if it becomes balanced, increase matches.

17.   Check If We Found a Match
        if matches == 26:
            return True
After updating both sides of the window, if all 26 letters are balanced, this window is a permutation. Return True.

***Let's Trace Our Example***
Initial window: indices 0-1 → "ei"
matches = 22 → not found.

i = 2:
Add 'd' (index 3): diff[3] goes 0 → -1 (matches drops to 21)
Remove 'e' (index 4): diff[4] goes -1 → 0 (matches goes back to 22)
Window = "id" → still not found.

i = 3:
Add 'b' (index 1): diff[1] goes 1 → 0 (matches increases to 23)
Remove 'i' (index 8): diff[8] goes -1 → 0 (matches increases to 24)
Window = "db" → not found yet.

i = 4:
Add 'a' (index 0): diff[0] goes 1 → 0 (matches increases to 25)
Remove 'd' (index 3): diff[3] goes -1 → 0 (matches increases to 26)
Now matches == 26 → Return True! ✅
The window is indices 3-4 → "ba", which is a permutation of "ab".

🏁 Final Line
python
        return False
If we finish the whole loop and never found matches == 26, it means no window was a permutation. Return False.

"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        a = ord("a")
        diff = [0] * 26

        for i in range(n1):
            diff[ord(s1[i]) - a] += 1
            diff[ord(s2[i]) - a] -= 1

        matches = 0
        for x in diff:
            if x == 0:
                matches += 1

        if matches == 26:
            return True

        for i in range(n1, n2):
            ind_in = ord(s2[i]) - a
            if diff[ind_in] == 0:
                matches -= 1
            diff[ind_in] -= 1
            if diff[ind_in] == 0:
                matches += 1

            ind_out = ord(s2[i - n1]) - a
            if diff[ind_out] == 0:
                matches -= 1
            diff[ind_out] += 1
            if diff[ind_out] == 0:
                matches += 1

            if matches == 26:
                return True

        print(matches)
        return False
