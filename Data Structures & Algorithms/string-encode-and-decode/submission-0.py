'''
    line: return ''.join(f"{len(s)}#{s}" for s in strs)

for s in strs → Loop through each string in the input list.
f"{len(s)}#{s}" → For each string s, create a formatted string:
len(s) → gets the length (e.g., 5).
# → a delimiter.
s → the original string itself.
Example: "hello" → "5#hello".
''.join(...) → Take all those formatted chunks and concatenate them together with nothing (empty string) in between.
Result: "5#hello5#world" for ["hello", "world"].

    line: length = int(s[i:j])

s[i:j] → slices the substring from i to j-1 (the digits representing the length).
Example: if i=0 and j=1, s[0:1] is "5".
int(...) → converts that digit string to an integer (e.g., "5" → 5).
This length tells us exactly how many characters the original string had.

    line: i = j + 1 + length
Moves the main pointer i to the start of the next chunk.
j + 1 moves past the delimiter, and + length moves past the entire string content.
Now i points to the first digit of the next length (or equals len(s) if this was the last chunk).

    line: res.append(s[j+1:i])
j+1 → the index right after the # delimiter. This is where the actual string content begins.
j+1+length → the index where the actual string ends (exclusive).
s[j+1:j+1+length] → slices exactly length characters starting after the #.
Example: if s = "5#hello", j=1, length=5 → s[2:2+5] = s[2:7] = "hello".
.append(...) → adds this extracted string to the res list.

Time Complexity : O(N)
Space Complexity: O(N)

'''

class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != '#':
                j += 1
            length = int(s[i:j])

            res.append(s[j+1:j+1+length])
            i = j+1+length
        return res
