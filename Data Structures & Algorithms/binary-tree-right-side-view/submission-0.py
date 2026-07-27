'''
Essentially, you need to return the last node of every level in a level-order traversal.

    Core Idea:
You have two standard approaches. The BFS (Queue) approach is the most intuitive, but the DFS approach is surprisingly elegant.

    Approach 1: BFS (Level Order) – Most Common
Perform a standard level-order traversal. For each level, traverse all nodes from left to right. When you finish the level, the last node you popped is the rightmost one. Add that node's value to the result.

    Approach 2: DFS (Pre-order with Right Priority) – Most Elegant
Perform a modified pre-order traversal: Root → Right → Left. Maintain a depth counter. If the current depth equals the size of the result list, it means this is the first node visited at this depth (and because we go right first, it's guaranteed to be the rightmost view). Append it.

    Complexity
Approach	    Time	Space	Notes
BFS (Queue)	    O(n)	O(n)	Queue holds up to the widest level (≈ n/2).
DFS (Recursive)	O(n)	O(h)	Call stack uses height (O(log n) balanced, O(n) skewed). Better space on average.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        result = []

        def dfs(node, depth):

            if not node:
                return []

            if depth == len(result):
                result.append(node.val)

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)    

        dfs(root, 0)
        return result
        

'''
BFS:
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            rightmost = None
            
            for i in range(level_size):
                node = queue.popleft()
                rightmost = node.val  # Keep overwriting; last one remains
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(rightmost)  # After the level ends, rightmost holds the rightmost value
        
        return result
'''