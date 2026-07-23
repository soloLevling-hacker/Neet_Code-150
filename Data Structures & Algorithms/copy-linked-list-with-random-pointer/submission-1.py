'''
Part 1: The Node Class

class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

This defines the structure of a single node in our linked list.
val stores the integer value.
next is a pointer to the next node in the list (normal linked list behavior).
random is the special pointer that can point to any node in the list (or None).

Part 2: The Function Definition & Edge Case

def copyRandomList(head):
    if not head:
        return None

head is the starting node of the original list.
Why this check? If the original list is empty (i.e., head is None), there is nothing to copy. We simply return None. This prevents our code from crashing later.

Part 3: The Phonebook (Dictionary)

    old_to_new = {}
    
This is the most important line in the entire solution.
We create an empty dictionary. Think of it as a translator or phonebook.
Key = An original node from the old list.
Value = The brand-new copy of that node.
Why do we need this? Because when we are building the random and next pointers for our new nodes, we need to instantly find the copy of a node that the original is pointing to.

Part 4: The First while Loop (Creating the Clones)

    curr = head
    while curr:
        old_to_new[curr] = Node(curr.val)
        curr = curr.next

Let's walk through this loop step-by-step:
curr = head → We start at the very beginning of the original list.
while curr: → Keep looping until we reach the end (None).
The Magic Line: old_to_new[curr] = Node(curr.val)
We look at the current original node (curr).
We create a brand new Node object with the exact same value (curr.val).
We store this new node into our dictionary, using the original node as the key.
curr = curr.next → Move to the next original node.

Crucial point to understand:
At the end of this first loop, we have created all the new nodes, but they are not connected to each other yet. Their next and random pointers are still set to None (because we didn't pass them in the constructor). The dictionary looks like this in memory:

Original List:   A(original) -> B(original) -> C(original)

Dictionary: {
   A(original) : A'(brand new copy),
   B(original) : B'(brand new copy),
   C(original) : C'(brand new copy)
}

Part 5: The Second while Loop (Wiring the Connections)

    curr = head
    while curr:
        copy_node = old_to_new[curr]
        copy_node.next = old_to_new.get(curr.next)
        copy_node.random = old_to_new.get(curr.random)
        curr = curr.next

Now we traverse the original list a second time. This time, we use the dictionary to hook up the pointers.
curr = head → Reset to the start of the original list.
copy_node = old_to_new[curr] → Look in the dictionary. "Hey dictionary, give me the brand new copy that belongs to this current original node." We store that copy in a variable called copy_node.
Wiring the next pointer: copy_node.next = old_to_new.get(curr.next)
Look at the original node curr. Where does its next point? It points to the original next node (curr.next).
We ask our dictionary: "Give me the brand-new copy of that original next node."
We set our copy_node's next to this result.
Why .get() instead of []? If curr.next is None (meaning we are at the end of the list), using old_to_new[None] would crash the program because None is not a key in our dictionary. Using .get() safely returns None instead of crashing, which is exactly what we want (next = None).
Wiring the random pointer: copy_node.random = old_to_new.get(curr.random)
Look at the original node curr. Where does its random point? It might point to some node, or it might be None.
Again, we ask the dictionary: "Give me the brand-new copy of that original random node."
We set our copy_node's random to this result.
If curr.random is None, .get() safely returns None.
curr = curr.next → Move to the next original node.

Why this works perfectly:
By the time we run this second loop, every copy node already exists in the dictionary. So when we wire A' (the copy of A), and its random points to B(original), we can instantly grab B' (the copy of B) from the dictionary and connect them.

Part 6: Returning the Answer

    return old_to_new[head]

head is the original starting node.
old_to_new[head] looks up the dictionary and returns the brand-new copy of the head node.
Because we perfectly wired all the next and random pointers in the second loop, returning this single node automatically gives us the entire deep-copied linked list.
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return
            
        old_to_new = {}

        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            copy = old_to_new[curr]
            copy.next = old_to_new.get(curr.next)
            copy.random = old_to_new.get(curr.random)
            curr = curr.next

        return old_to_new[head]