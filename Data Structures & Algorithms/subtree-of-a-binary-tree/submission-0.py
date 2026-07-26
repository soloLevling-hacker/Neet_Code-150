'''
    Intuition & Core Insight:
The Problem:
We have a big tree (root) and a small tree (subRoot). We need to check if the small tree exists exactly somewhere inside the big tree.

The Key Realization:
A subtree is defined by a specific node AND all of its descendants.
This means we can break the problem into two smaller tasks:

Traversal: We must visit every single node in root because subRoot could start anywhere.

Comparison: At each node, we ask: "Does the tree starting right here exactly match subRoot?"
Because we already solved the "Same Tree" problem (checking exact equality), we can reuse that logic as a helper tool inside our traversal.

2. The "Why" Behind the Approach:
Decision	                        Why?
Use DFS (Pre-order) Traversal	    Subtree definitions are recursive. Starting at the root, checking left, then right (Pre-order: root → left → right) is the most natural way to search.
Reuse isSameTree	                Keeps code clean and avoids duplication. The isSameTree function handles the "exact match" logic perfectly.
Return True immediately on match	Optimizes performance. As soon as we find the subtree, we stop searching (short-circuiting).
Use or when recursing left/right	The subtree only needs to be found on one side. If it's on the left, we don't need to check the right (or does this automatically).
Handle not subRoot first	        Edge case: An empty tree is technically a subtree of everything.
Handle not root second	            Edge case: We've reached the end of the big tree without finding the small one.

3. Algorithm Steps (Formal):
Pre-check: If subRoot is None → return True.
Pre-check: If root is None (but subRoot isn't) → return False.
Compare current node: Call isSameTree(root, subRoot).
If True, we found it! Return True.
Recursive search: Check the left child OR the right child.
Return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot).

Inside isSameTree (Exact Match):
If both p and q are None → True.
If only one is None → False.
If p.val != q.val → False.
Otherwise, check left and right using and (both must match).


    Complexity Analysis (Structured):
m = nodes in root, n = nodes in subRoot.

Complexity	        Value	                                    Explanation
Time (Worst Case)	O(m * n)	                                Example: A skewed tree where isSameTree traverses deep into n nodes at every level before failing on the very last leaf, repeated for all m nodes.
Time (Average)	    O(m + n)           	                        In most balanced trees, the isSameTree check fails immediately at the root (due to value mismatch), making it O(1) per node. Thus average is O(m).
Space	            O(max(height of root, height of subRoot))	This is the recursion stack depth. In a skewed tree, this could be O(m + n).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot:
            return True

        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: TreeNode, q: TreeNode):

        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)