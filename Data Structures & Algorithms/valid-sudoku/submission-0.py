'''
1. The Setup (The Data Structures)
rows = [set() for _ in range(9)]
cols = [set() for _ in range(9)]
boxes = [set() for _ in range(9)]
We create 3 lists, each containing 9 empty Python set() objects.

Why a set? Sets provide O(1) average time lookups. When we see a number, we just ask, "Have I seen this number before in this specific row/column/box?" If the answer is yes, the board is invalid.
rows[0] = set of digits currently seen in row 0.
cols[5] = set of digits currently seen in column 5.
boxes[4] = set of digits currently seen in 3x3 sub-box number 4.

2. The Nested Loop (Traversal)
for r in range(9):
    for c in range(9):
        val = board[r][c]

This iterates from top-left (0,0) to bottom-right (8,8), moving left-to-right, top-to-bottom.
When we hit a '.', we skip it because empty cells don't violate any rules.

3. The Row and Column Checks (Straightforward)
if val in rows[r]:
    return False
rows[r].add(val)

if val in cols[c]:
    return False
cols[c].add(val)

For the current cell (r, c), we check if val already exists in the set for that specific row.
If it does, duplicate in the row → Invalid.
If not, we add it to the row's set so future cells in this row know about it.
We do exactly the same for the column using cols[c].

4. The 3x3 Box Check (The "Magic" Formula)
box_idx = (r // 3) * 3 + (c // 3)
This is the most confusing part for many. Let's decode it.
r // 3 gives us the row-group (0, 1, or 2).
c // 3 gives us the column-group (0, 1, or 2).
Multiplying the row-group by 3 and adding the column-group gives a unique ID (0 to 8) for each box.

Visualization of box_idx:
Box 0	Box 1	Box 2
Box 3	Box 4	Box 5
Box 6	Box 7	Box 8

Let's test the formula with real coordinates:
Cell (0, 2): (0 // 3) * 3 + (2 // 3) = 0 * 3 + 0 = Box 0 ✅
Cell (1, 4): (1 // 3) * 3 + (4 // 3) = 0 * 3 + 1 = Box 1 ✅
Cell (4, 7): (4 // 3) * 3 + (7 // 3) = 1 * 3 + 2 = Box 5 ✅
Cell (8, 8): (8 // 3) * 3 + (8 // 3) = 2 * 3 + 2 = Box 8 ✅
Once we get this unique Box ID, we do the exact same check: "Has this value been seen in this box before?"

5. Step-by-Step Walkthrough (Example)
Imagine we are looking at a board that has a duplicate '5' in the top row.
Cell (0, 0) = '5'
rows[0] is empty → add '5'.
cols[0] is empty → add '5'.
box_idx = 0 → boxes[0] is empty → add '5'.
... (process other cells)
Cell (0, 3) = '5'
rows[0] currently has {'5'}.
Check: if '5' in rows[0]: → True.
The function immediately returns False. We don't even need to check the column or box because a single violation makes the whole board invalid.

6. Why is this algorithm so efficient?
Time Complexity: Technically O(81) because there are exactly 81 cells. Since 81 is a constant (the board is always 9x9), we simplify this to O(1). It never scales up.
Space Complexity: We store at most 9 digits in each of the 27 sets. That's a maximum of 81 integers stored across all sets, which is also a constant O(1).
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        raws = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == '.':
                    continue
                
                if val in raws[r]:
                    return False
                raws[r].add(val)

                if val in cols[c]:
                    return False
                cols[c].add(val)

                box_id = (r // 3)*3 + (c // 3)

                if val in boxs[box_id]:
                    return False
                boxs[box_id].add(val)

        return True