'''
Binary Tree Level Order Traversal (also known as Breadth-First Search or BFS) is the process of visiting every node in a binary tree level by level, from top to bottom, and left to right within each level.
Here is a complete, practical guide covering the standard implementation, variations, and complexity analysis.

    Core Idea:
To traverse level by level, you need to process nodes in the order they are discovered. The perfect data structure for this is a Queue (FIFO).

    Algorithm:
Push the root node into a queue.
While the queue is not empty:
Record the current size of the queue (levelSize). This tells you exactly how many nodes are on the current level.
Pop levelSize nodes from the front of the queue.
For each popped node, add its value to the current level's list, and push its left and right children (if they exist) to the back of the queue.
Move to the next level.

    Complexity
Time: O(n) – each node is visited exactly once.
Space: O(n) – the queue holds at most the maximum number of nodes at any level. In a perfect binary tree, the last level has roughly n/2 nodes, so space is O(n).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            length = len(queue)
            current_level = []

            for _ in range(length):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)

        return result