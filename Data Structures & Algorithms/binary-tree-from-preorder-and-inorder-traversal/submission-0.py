'''
    NOTES:
In preorder, the first element is always the root of the tree.
Once we know the root value, we can find its position in the inorder array.
Everything to the left of that position in inorder belongs to the left subtree, and everything to the right belongs to the right subtree.
Recursively apply the same logic to build the left and right subtrees.

    Approach (Recursive with Hash Map):
Build a hash map from value to its index in inorder → O(1) lookup later.
Use a global/closure variable pre_idx to track the next root in preorder.
Define a recursive function build(left, right) that builds the subtree from inorder[left:right] (half‑open interval).
If left == right, there are no nodes → return None.
Pick the next value from preorder using pre_idx, increment it.
Create a TreeNode with that value.
Find the index mid of this value in inorder using the hash map.

Recursively build:
root.left = build(left, mid)
root.right = build(mid + 1, right)
Return the root.
Initially call build(0, len(inorder)).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0

        def build(left, right):
            
            nonlocal pre_idx

            if left == right:
                return None

            root_val = preorder[pre_idx]
            pre_idx += 1

            root = TreeNode(root_val)

            mid = inorder_map[root.val]

            root.left = build(left, mid)
            root.right = build(mid + 1, right)

            return root


        return build(0, len(inorder))

'''
    Example Walkthrough:
Input:

preorder = [3, 9, 20, 15, 7]
inorder  = [9, 3, 15, 20, 7]

Step 1:
inorder_map = {9:0, 3:1, 15:2, 20:3, 7:4}
pre_idx = 0

Step 2:
build(0, 5)
root_val = preorder[0] = 3 → pre_idx = 1
mid = inorder_map[3] = 1
root = 3

Step 3:
root.left = build(0, 1)
root_val = preorder[1] = 9 → pre_idx = 2
mid = inorder_map[9] = 0
root = 9
build(0,0) → None and build(1,1) → None
returns node 9

Step 4:
root.right = build(2, 5)
root_val = preorder[2] = 20 → pre_idx = 3
mid = inorder_map[20] = 3
root = 20

root.left = build(2, 3)
root_val = preorder[3] = 15 → pre_idx = 4
mid = inorder_map[15] = 2
returns node 15

root.right = build(4, 5)
root_val = preorder[4] = 7 → pre_idx = 5
mid = inorder_map[7] = 4
returns node 7
returns node 20

Final tree:

     3
    / \
   9   20
      /  \
     15   7

    Complexity:
Time:  O(n) – each node is processed once, and hash map lookups are O(1).
Space: O(n) – hash map stores n entries plus recursion stack O(h) where h is tree height (worst-case O(n) for skewed tree).

    Important Notes:
This algorithm assumes all values are distinct. If duplicates exist, multiple trees could satisfy the traversals, and the problem becomes ill‑posed.
The iterative version using a stack also exists, but the recursive approach is the most intuitive and widely used.
'''