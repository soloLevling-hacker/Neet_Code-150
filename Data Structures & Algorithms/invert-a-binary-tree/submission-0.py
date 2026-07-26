'''
Approach & Explanation
Problem Statement:
Given the root of a binary tree, invert the tree and return its root. Inverting means swapping the left and right children for every node, creating a mirror image of the original tree.

Intuition:
Think of a binary tree as a collection of smaller subtrees. If we can figure out how to swap the children of a single node, we can apply the exact same logic to every node in the entire tree. This makes recursion the perfect fit because the structure repeats itself.

Algorithm Steps:
Base Case
Check if the current node is None. If it is, return None. This handles empty trees and prevents the function from trying to access children of a leaf node.

Swap the Children
For the current node, swap its left and right child references.
(In Python, a, b = b, a does this instantly without needing a temporary variable.)

Recurse on the Left Subtree
Call invertTree on the new left child (which was originally the right child). This will invert that entire subtree.

Recurse on the Right Subtree
Call invertTree on the new right child (which was originally the left child). This inverts that entire subtree.

Return the Current Node
After both subtrees are inverted, return the current node. This allows the parent call to receive the updated subtree.

Traversal Order
We follow a Pre-order (Depth-First) pattern:
Process the current node (swap).
Go left.
Go right.
(Note: For this specific problem, swapping before or after the recursive calls still works because the swaps are independent, but pre-order is the most intuitive.)

Complexity Analysis:
Time Complexity: O(n)
We visit every single node in the tree exactly once. n is the total number of nodes.

Space Complexity: O(h)
The recursion stack uses space proportional to the height of the tree (h).
Best case (balanced tree): O(log n)
Worst case (skewed tree like a linked list): O(n)
Visual Dry Run (Example)

Input Tree:
     4
   /   \
  2     7
 / \   / \
1   3 6   9

Step-by-step:
root = 4 → Swap children → left=7, right=2.
Recurse on left (7) → Swap children → left=9, right=6.
Recurse on right (2) → Swap children → left=3, right=1.

Final Output Tree:
     4
   /   \
  7     2
 / \   / \
9   6 3   1

Key Takeaway
The algorithm does not change the integer values inside the nodes. It only changes the connections (pointers) between the nodes, effectively repositioning entire subtrees in a single swap operation.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root