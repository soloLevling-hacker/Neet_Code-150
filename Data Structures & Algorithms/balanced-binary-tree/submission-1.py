'''
    Why is Balance Important?
Search/Insert/Delete complexity degrades to O(n) in a skewed tree.
A balanced tree keeps height ≤ O(log n), ensuring operations run in O(log n) time.
Used in AVL trees, Red‑Black trees, and B‑trees.

    Checking if a Binary Tree is Balanced:
Approach:
We can compute the height of each subtree while simultaneously checking balance. Instead of computing height separately (which would be O(n²) due to repeated traversals), we use a bottom‑up DFS that returns:
-1 if the subtree is unbalanced
the height of the subtree if balanced
This yields O(n) time and O(h) recursion stack space (h = tree height).

    Algorithm (Recursive):
If root is null, return height 0 (balanced).
Recursively check left subtree → get leftHeight.
Recursively check right subtree → get rightHeight.
If either subtree is unbalanced (-1) or |leftHeight - rightHeight| > 1, return -1.
Otherwise, return max(leftHeight, rightHeight) + 1.
At the end, the tree is balanced if the recursive call returns -1 or not.

    NOTES:
Scenario A: The left subtree is personally broken at its root:
This happens when the child subtree is balanced internally, but the root of that child subtree has a height difference greater than 1 between its own two children.

Tree shape that causes this:
        (Current Node)
         /      \
    [Left Child]  (anything)
      /    \
    (A)    (B)
    /
   (C)

Let's say Current Node calls check(Left Child).
Inside check(Left Child):
Left child of Left Child (Node A) returns height 2.
Right child of Left Child (Node B) returns height 0 (null).
abs(2 - 0) > 1 → TRUE.
So check(Left Child) executes return -1.
Result: That -1 is what gets assigned to the original left variable.

Scenario B: The left subtree contains a broken node deeper inside it:
This happens when the root of the left subtree is perfectly fine, but it detected a -1 coming from its own child. It simply forwards the message up.

Tree shape that causes this:
        (Current Node)
         /      \
    [Left Child]  (anything)
      /    
   (Grandchild)
      /
     (Great-Grandchild)
      \
       (Great-Great)

Inside check(Left Child):
It calls check(Grandchild).
Grandchild checks its children, sees a height difference > 1, and returns -1 to Left Child.
Left Child sees if left == -1, immediately executes return -1 without checking anything else.
Result: That -1 is passed up and assigned to the original left variable.

Summary table for "What gives -1 to my variable?"
If you wrote this line:	The variable gets -1 when...
left = check(node.left)	The root of the left subtree (or any node inside it) has a height difference > 1.
right = check(node.right)	The root of the right subtree (or any node inside it) has a height difference > 1.

The most important point for your understanding:
The variable left is supposed to hold a height (like 2 or 3).
But if the tree is broken, the function says: "I refuse to give you a fake height for a broken tree. Here is -1 as a warning signal instead."
So left only gets -1 when the subtree you just asked about is NOT balanced. If the subtree is balanced, left will always be 0, 1, 2, 3... (a real height).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node: Treenode):
            if not node:
                return 0
            
            left_h = check(node.left)
            if left_h == -1:
                return -1
            
            right_h = check(node.right)
            if right_h == -1:
                return -1
            
            if abs(left_h - right_h) > 1:
                return -1

            return max(left_h, right_h) + 1
        return check(root) != -1