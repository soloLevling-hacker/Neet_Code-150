'''
Approach & Explanation:
Problem Statement
Given the root of a binary tree, return its maximum depth. The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Intuition:
Imagine you are standing at the top of a tree and want to know how many levels it has. Instead of counting the whole tree at once, you ask your left child and right child: "How deep are you?" They ask their children, and so on, until they reach the ground (empty nodes). Each node simply adds 1 (itself) to the deepest answer it receives from its children. This is a classic divide-and-conquer recursion.

Algorithm Steps:
Base Case:
If the current node is None (empty), return 0. This represents zero depth.
(This also handles an empty input tree gracefully.)

Recursively Find Depth of Left Subtree
Call maxDepth on the left child. This returns the total number of levels present in the left side.

Recursively Find Depth of Right Subtree
Call maxDepth on the right child. This returns the total number of levels present in the right side.

Combine the Results:
Take the larger of the two depths (left or right) and add 1 to account for the current node itself.
Return this final number.

Traversal Order (Post-order):
We process the children first and then use their results to figure out the answer for the current node. This is known as a Post-order (bottom-up) traversal.

Complexity Analysis
Time Complexity: O(n)
Every single node in the tree is visited exactly once, where n is the total number of nodes.

Space Complexity: O(h)
The recursion stack uses space proportional to the height of the tree (h).
Best case (balanced tree): O(log n)
Worst case (skewed tree like a linked list): O(n)
Visual Dry Run (Example)

Input Tree:
     3
   /   \
  9    20
      /  \
     15   7

Step-by-step breakdown (bottom-up):
Node 15: left=0, right=0 → max(0,0)+1 = 1
Node 7: left=0, right=0 → max(0,0)+1 = 1
Node 20: left depth = 1 (from 15), right depth = 1 (from 7) → max(1,1)+1 = 2
Node 9: left=0, right=0 → max(0,0)+1 = 1
Root 3: left depth = 1 (from 9), right depth = 2 (from 20) → max(1,2)+1 = 3
Final Answer: 3 (The longest path is 3 -> 20 -> 15 or 3 -> 20 -> 7).

Key Takeaway
This algorithm works because the depth of a tree is simply: 1 (for the root) + the deepest depth among its two subtrees. Recursion allows us to break this problem down into the smallest possible pieces (leaf nodes) and build the answer back up.

Note:
return 0 is the base case – it tells us that an empty node contributes zero depth and stops further recursion.
For every non‑empty node, we ask both children for their maximum depth, then add 1 to the larger answer to count the current node itself.
This builds the total depth from the bottom up – leaves return 1, their parents return 2, and so on until the root gives the final answer.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        max_depth = max(left_depth, right_depth) + 1
        return max_depth