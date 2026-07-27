'''
    A binary search tree satisfies the following constraints:
The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.

    Kth Smallest Integer in BST:
Given the root of a Binary Search Tree and an integer k (1-indexed), find the k-th smallest value among all node values.
Since an in‑order traversal of a BST visits nodes in strictly ascending order, the k-th element visited is the answer.

    Key Insight:
Perform an in‑order traversal (left → root → right).
Maintain a counter or a stack.
Stop when you've visited k nodes.

    Approaches:
    1. Recursive In‑order (with early stopping)
Traverse recursively, decrement k at each node. When k == 0, the current node is the answer.
Time: O(n) in worst case (if k = n), but can stop early.
Space: O(h) recursion stack.

    2. Iterative In‑order (with stack) – Recommended
Simulate the in‑order traversal using an explicit stack. This avoids recursion limits and stops as soon as the k-th node is popped, giving O(h + k) time.
Time: O(h + k) — h is tree height, k is the rank.
Space: O(h) for the stack.

    3. Augmented BST (subtree sizes)
If the tree nodes store the size of their left subtree, you can decide whether to go left, right, or return the current node in O(log n) time. This is useful when the tree is static and many queries are performed.
(I will mention this briefly but focus on the standard O(n) / O(h+k) solutions.)

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.result = None
        def dfs(node):
            if not node or self.k == 0:
                return 
            
            dfs(node.left)
            self.k -= 1
            if self.k == 0:
                self.result = node.val
            
            dfs(node.right)
            
        dfs(root)
        return self.result

'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root: TreeNode, k: int) -> int:
    stack = []
    curr = root
    
    while stack or curr:
        # Go as far left as possible
        while curr:
            stack.append(curr)
            curr = curr.left
        
        # Visit the smallest unvisited node
        curr = stack.pop()
        k -= 1
        if k == 0:
            return curr.val
        
        # Move to the right subtree
        curr = curr.right
    
    return -1  # Should never reach if k is valid


    Advanced Option: Augmented BST (Subtree Sizes):
If nodes store leftSize (number of nodes in left subtree), the algorithm becomes:

def kthSmallest(root, k):
    while root:
        left_count = root.left.size if root.left else 0
        if k == left_count + 1:
            return root.val
        elif k <= left_count:
            root = root.left
        else:
            k -= left_count + 1
            root = root.right
'''
