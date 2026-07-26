'''
Input: p = [4,7], q = [4,null,7]
Output: false

    The Core Logic (Recursive DFS):
We traverse both trees simultaneously, node by node. At each step, we check 3 things:
Are both nodes null? → If yes, they match here. Return True.
Is exactly one of them null? → If yes, the structures differ. Return False.
Do the values differ? (p.val != q.val) → If yes, they don't match. Return False.

If all above pass, this node is identical. Now recursively check:
Left child of Tree 1 vs Left child of Tree 2
Right child of Tree 1 vs Right child of Tree 2
Both must be True for the trees to be the same.


    NOTES:
Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.


'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)