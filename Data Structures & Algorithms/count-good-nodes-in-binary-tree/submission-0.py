'''
A node is good if its value is greater than or equal to the maximum value encountered from the root down to that node.

1. Core Idea
As you traverse from the root downwards, keep track of the maximum value seen so far on that path.
Root is always good (since there are no nodes before it to be greater).
For any other node, compare node.val against current_max:
If node.val >= current_max → It is good (count it), and update current_max = node.val.
Else → Not good. Keep current_max unchanged.
Recurse into left and right children, passing the updated current_max.

    Algorithm (DFS Pre-order)
Initialize count = 0.
Start DFS from root with max_so_far = -inf (or root.val).
At each node:
If node.val >= maxi:
Increment count.
Update maxi = node.val.
Recurse to left child with maxi.
Recurse to right child with maxi.
Return the count.

    Complexity
Approach	    Time	Space	Notes
DFS (Recursive)	O(n)	O(h)	Call stack height (O(log n) balanced, O(n) skewed).
DFS (Iterative)	O(n)	O(n)	Stack holds tuples of (node, max_so_far).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        count = 0
        def dfs(node, maxi):
            nonlocal count
            if not node:
                return 0
            
            if node.val >= maxi:
                count += 1
                maxi = node.val
            dfs(node.left, maxi)
            dfs(node.right, maxi)

        dfs(root, float('-inf'))    
        return count