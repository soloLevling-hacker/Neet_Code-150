'''
1. The Core Strategy (One Sentence)
We create a fake "anchor" node, then use a moving "finger" (tail) to repeatedly pick the smallest front node from either list, hook it to the end, and walk forward—all by manipulating memory addresses.

2. The Code (Our Reference Map)
def mergeTwoLists(list1, list2):
    dummy = ListNode()   # Anchor at memory address 0x000
    tail = dummy         # Sticky note pointing to 0x000

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1   # Hook list1's address into the chain
            list1 = list1.next  # Move input pointer forward
        else:
            tail.next = list2   # Hook list2's address into the chain
            list2 = list2.next  # Move input pointer forward
        tail = tail.next        # Move the sticky note to the new last node

    tail.next = list1 if list1 else list2  # Glue the leftovers
    return dummy.next  # Skip the fake anchor, give the real head

3. The 3 Pillars of Understanding (Your Knowledge Applied)

Concept	Analogy	Code & Memory
Dummy Node	        A nail hammered into the table before we start building the chain. We never give it to the user.	   Fixed address (e.g., 0x000). We always return dummy.next.
Tail Variable	    A sticky note (post-it) we slide forward. It always sticks to the last link of our finished chain.	   tail holds an address. tail = tail.next overwrites the sticky note.
Node.next	        The physical metal hook on a chain link. Once we set it, it permanently points to the next link.	   tail.next = list1 writes an address into the node's next storage box.

Crucial Distinction (You already know this!):
tail.next = X → Writing an address into a node. (Builds the chain).
tail = tail.next → Moving the sticky note to the address X. (Does NOT change the chain).

4. Full Step-by-Step Example (The "EX" Part)
Let's merge:
List 1: [1 -> 3] → Node(1) at address 0x100, Node(3) at address 0x104.
List 2: [2 -> 4] → Node(2) at address 0x200, Node(4) at address 0x204.

Initial Setup
Variable	Memory Address it holds
dummy	    0x000 (Fake anchor)
tail	    0x000 (Sticky note on anchor)
list1	    0x100 (Head of list 1)
list2	    0x200 (Head of list 2)
Visual: [dummy:0x000] ← tail is here.

Iteration 1
Compare: 1 (0x100) vs 2 (0x200). Pick 0x100.
Action 1 (tail.next = list1): Go to address 0x000 (dummy) and write 0x100 into its next box.
Action 2 (tail = tail.next): Move the sticky note. tail now holds 0x100.

Memory State	Visual Result
dummy.next is now 0x100	[dummy] → [1]

Iteration 2
Compare: 3 (0x104) vs 2 (0x200). Pick 0x200.
Action 1 (tail.next = list2): Go to address 0x100 (Node 1) and write 0x200 into its next box.
Action 2 (tail = tail.next): Move sticky note. tail now holds 0x200.

Memory State	Visual Result
Node(1).next is now 0x200	[dummy] → [1] → [2]

Iteration 3
Compare: 3 (0x104) vs 4 (0x204). Pick 0x104.
Action 1 (tail.next = list1): Go to address 0x200 (Node 2) and write 0x104 into its next box.
Action 2 (tail = tail.next): Move sticky note. tail now holds 0x104.

Memory State	Visual Result
Node(2).next is now 0x104	[dummy] → [1] → [2] → [3]

Loop Ends (list1 became None)
Action (tail.next = list2): Go to address 0x104 (Node 3) and write 0x204 into its next box. (Glue the rest).
Return (dummy.next): Return 0x100, which is the head of our new chain.

Final Memory	Visual Final Result
Node(3).next is now 0x204	[dummy] → [1] → [2] → [3] → [4]

5. The Edge Cases (With Your Memory Knowledge)
Scenario	                        What happens in memory
Both lists are None	                dummy.next remains 0x000 (None). We return None. Safe.
One list is empty	                The while loop never runs. tail is still at dummy (0x000). tail.next = list1 or list2 writes the other list's starting address directly into dummy.next. Return that address.
Duplicate values (e.g., 1 vs 1)	    Using <= means we pick list1 first. We write its address, then later list2's address. Both get hooked in order (stable merge).

6. Complexity Through Memory Lenses
Metric	Why?
Time: O(n + m)	   We visit every single memory address (node) exactly once inside the loop.
Space: O(1)	       We never use new ListNode() inside the loop. We only move around existing memory addresses. The dummy and tail are the only 2 extra memory boxes we create.

7. Final Takeaway (Burn this into your brain)
tail.next = something writes a memory address into a node, permanently extending the data structure.
tail = something rewrites the address on your sticky note, moving your position without touching the structure.
'''


#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:

            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 if list1 else list2

        return dummy.next