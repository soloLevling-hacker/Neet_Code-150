'''
    Approach & Explanation:
Problem Statement:
Given the root of a binary tree, return the length of its diameter. The diameter is the number of edges along the longest path between any two nodes in the tree. This path may or may not pass through the root.

Intuition:
The longest path between two nodes will always go up from a node on the left side to some "meeting point" and then down to a node on the right side. For any node, the longest path that passes through it is simply:
height of its left subtree + height of its right subtree (measured in edges).
If we can compute the height of every node, we can check this sum at every node and keep track of the largest one globally.

Algorithm Steps:
Global Tracker
Create a variable diameter to store the maximum path length found so far.
Define a Recursive Function height(node)

Base Case:
If node is None, return 0 (an empty subtree has zero height in terms of nodes).

Recurrence:
Recursively find the height of the left child (left_h).
Recursively find the height of the right child (right_h).

Update the Diameter:
The path that passes through the current node has length left_h + right_h (edges). Update diameter = max(diameter, left_h + right_h).

Return to Parent:
Return max(left_h, right_h) + 1 (the height of the current subtree in nodes).

Start the Recursion
Call height(root) to process the entire tree.

Return the Result
Output the final diameter.

NOTES:
    The Golden Rule to Remember:
The function must fully solve the left subtree before it is allowed to even look at the right subtree.
So the travel order is:
Root → Deepest Left Leaf → ... → Back Up → Right Leaf → ... → Back Up → Root's Right Side → ... → Back to Root for Final Check.
This is the definition of Depth-First Search (DFS). It goes as deep as possible down one branch before it ever touches the other branch.


    The Core Concept:
Diameter = The longest path between any two nodes in the tree.
We count the number of edges (lines connecting nodes).
This path does NOT have to pass through the root. It could be hidden deep inside a subtree.

    The 3 Most Confusing Things:
A. Why nonlocal diameter?
We use diameter = inside the height function. This tries to change the outer variable.
Python has a rule: If you use = on a variable inside a function, it creates a new local variable unless you say otherwise.
nonlocal diameter tells Python: "Don't make a new one! Update the outer diameter variable."

B. Why return max(left_h, right_h) + 1?
This returns the Height (a one-way street).
When your parent asks "How tall are you?", you can only offer one single path going upward. You cannot split into two directions to go up!
So you pick the taller of your two children (max), add 1 for yourself, and send that upward.

C. Why diameter = max(diameter, left_h + right_h)?
This calculates the Diameter path (a two-way street).
The path can come up from the left child, pass through you, and go down to the right child. That uses both sides.
So we add them together (left_h + right_h) and check if this is bigger than the best diameter found so far.

D. Is this Top-Down or Bottom-Up?
Bottom-Up (Post-order).
The function starts at the root, but immediately dives down to the leaves.
The math (diameter = ... and return ...) only happens after the children have returned their heights. So the leaves check themselves first, then their parents, and the root checks itself last.

6. Complexity Analysis
Time: O(n) → We visit every single node exactly once.
Space: O(h) → The recursion stack uses memory equal to the height of the tree.
Balanced tree: O(log n)
Skewed tree (like a linked list): O(n)
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def height(node: TreeNode):
            nonlocal diameter
            if not node:
                return 0

            left_h = height(node.left)
            right_h = height(node.right)

            diameter = max(diameter, left_h + right_h)

            return max(left_h, right_h) + 1
        
        height(root)
        return diameter