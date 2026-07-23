'''
Approach:
1. Two‑Pass (Length + Removal)
Traverse the list to count its total length L.
The node to remove is at position L - n from the head (0‑based index).
Traverse again to find the node just before the target, adjust its next pointer.
Time: O(L) – two full passes
Space: O(1)

Drawback: Requires two traversals.

2. One‑Pass (Two Pointers / Sliding Window)
We can remove the node in a single pass by using two pointers with a fixed gap of n nodes.
Create a dummy node that points to head (this simplifies handling edge cases like removing the head).
Initialize two pointers: left and right, both pointing to the dummy node.
Move right forward n + 1 steps so that the gap between left and right is exactly n nodes.
Then advance both pointers one step at a time until right becomes None. At that moment, left is just before the node to remove.
Remove the target node by left.next = left.next.next.
Return dummy.next.

Why n + 1?
If we move right by n steps, then when right is at the last node, left would be at the node to remove (not before it). Moving n + 1 ensures left ends up one step before the target.
Time: O(L) – one pass
Space: O(1)

Step‑by‑step simulation
Initial list (with dummy node):

dummy(0) -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> None
left = dummy
right = dummy

Step 1: Move right forward n + 1 = 4 steps.
Move	right points to
Start	dummy
After 1	node 1
After 2	node 2
After 3	node 3
After 4	node 4

Now:
left is at dummy
right is at node 4
The gap between them is exactly 4 nodes (1, 2, 3, 4).

Step 2: Advance both pointers until right becomes None.
We'll move them together, one step at a time:
Iteration	left moves to	right moves to
    1	    node 1      	node 5
    2	    node 2      	node 6
    3	    node 3	        node 7
    4	    node 4	        node 8
    5	    node 5	        node 9
    6	    node 6      	node 10
    7	    node 7	        None (since 10 → None)
Stop. right is None.

Step 3: Remove the target.
left is now at node 7.
The node to remove is left.next, which is node 8.
We set left.next = left.next.next, so node 7 now points directly to node 9.

Final list:
dummy(0) -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 9 -> 10 -> None
Node 8 is removed. ✅
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        left = dummy
        right = dummy

        for _ in range(n + 1):
            right = right.next

        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next

        return dummy.next