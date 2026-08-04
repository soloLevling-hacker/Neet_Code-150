class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        n,m = len(board), len(board[0])

        def dfs(i, j, idx):

            if idx == len(word):
                return True
            if i<0 or i >= n or j<0 or j>=m or board[i][j] != word[idx]:
                return False
            
            tmp = board[i][j]
            board[i][j] = '#'

            found = (dfs(i+1, j, idx+1) or dfs(i-1, j, idx+1) or dfs(i, j+1, idx+1) or dfs(i, j-1, idx+1))

            board[i][j]=tmp
            
            return found

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and dfs(i,j,0):
                    return True
        return False

'''
    1.Approach (Step-by-Step):
The solution uses Backtracking (DFS) with in-place visited marking:

1.Find the starting point: Loop through every cell (i, j) on the board. Only when board[i][j] == word[0] do we start a DFS from that cell. This avoids needless searches.

2.Pass the current index: The DFS function takes (i, j, idx), where idx indicates which character of word we are currently trying to match.

3.Validate the current cell: At the start of DFS, immediately check if (i, j) is out of bounds or board[i][j] != word[idx]. If either is true, return False.
(Crucially, since we mark visited cells as '#', this single check handles both letter mismatches and revisiting the same cell).

4.Mark visited (in-place): Store the current cell’s value in temp, then overwrite board[i][j] = '#'. This marks it as used for the current path without needing a separate visited matrix.

5.Recursive exploration (Short-circuit OR): Recursively call DFS for the 4 neighbors (down, up, right, left) with idx + 1. Combine these with the or operator. Because or short-circuits, the moment one direction returns True, Python immediately stops checking the rest and propagates the True upward.

6.Backtrack: If all 4 directions return False, restore the cell back to its original character (board[i][j] = temp) and return False to allow other branches to use this cell later.

7.Victory condition: The success base case is at the top of DFS: if idx == len(word), return True. This means we found the last character in the previous call and incremented idx, so we immediately declare success without checking any board cells.

    2. Complexity Analysis:
Time Complexity: O(m * n * 3^L)
Where L is the length of the word. For each starting cell, we explore at most 3 new directions per step (we ignore the direction we came from). With m * n possible starting points, the theoretical upper bound is O(m * n * 3^L). In practice, pruning makes it significantly faster.

Space Complexity: O(L)
This accounts for the maximum depth of the recursion call stack. Since we modify the board in place (using '#') instead of allocating a separate visited set, the auxiliary space is O(1) aside from the recursion stack.
'''