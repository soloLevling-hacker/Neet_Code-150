'''
Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.

A valid binary search tree satisfies the following constraints:

The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.


    In‑order Traversal (Iterative or Recursive):
In a valid BST, an in‑order traversal (left → root → right) visits nodes in strictly increasing order.
So we can traverse and keep track of the previous node’s value. If at any point the current value ≤ previous, it’s invalid.
Time: O(n)
Space: O(h) for recursion stack, O(1) extra for iterative.

    Recursive Bounds (Min/Max):
Pass down an allowed range (low, high) for each node.
For the root, the range is (-∞, +∞).
For a left child, update the upper bound to the parent’s value.
For a right child, update the lower bound to the parent’s value.
If a node’s value violates its range, the tree is invalid.

Time: O(n)
Space: O(h) for recursion stack.

    Handling Duplicates:
The definition above uses strict inequality. If your problem allows equal values, adjust the bounds accordingly (e.g., <= or >=). In this answer we assume no duplicates.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, low, high):
            if not node:
                return True
            
            if not (low < node.val < high):
                return False
            
            return valid(node.left, low, node.val) and valid(node.right, node.val, high)

        return valid(root, float('-inf'), float('inf'))
