'''
1. What is the problem asking?
Imagine a linked list as a chain of boxes. Each box has a value and an arrow (pointer) pointing to the next box.
Given: 1 → 2 → 3 → 4 → 5
Goal: Take the first, then the last, then the second, then the second-last... until we meet in the middle.
Result: 1 → 5 → 2 → 4 → 3

Important Rule: We cannot create a new list or copy the values into an array. We must rearrange the existing arrows (pointers) to change the order. This is called "in-place" modification.

2. The Big Idea (The 4 Steps)
We can't just grab the last node easily because arrows only go forward. To get the last node, we would have to walk through the whole list every time—which is too slow.
So, we use a clever trick:
Cut the list into two halves.
Flip the second half backwards (so its last node becomes its first node).
Weave the first half and the flipped second half together.

3. Step-by-Step Breakdown

Step 1: Find the Middle
We use two pointers (arrows): Slow and Fast.
Slow moves 1 step at a time.
Fast moves 2 steps at a time.
When Fast reaches the end, Slow will be exactly at the middle.

Example: 1 → 2 → 3 → 4 → 5
Start: Slow=1, Fast=1
Move 1: Slow=2, Fast=3
Move 2: Slow=3, Fast=5
Move 3: Fast stops (can't move). Slow is at 3 (the middle). ✅

Step 2: Split the list into two halves
Now we have two separate chains:
First half: Starts at head (1), ends at slow (3).
Second half: Starts at slow.next (which is 4).
To split them, we do slow.next = None.
This removes the arrow from 3 to 4, breaking the chain into two:

First: 1 → 2 → 3
Second: 4 → 5

Step 3: Reverse the Second Half
We want to access the last node first. Since arrows only go forward, we flip the second half's arrows backwards.

Before reverse: 4 → 5
After reverse: 5 → 4

Now we have:
First: 1 → 2 → 3
Second (reversed): 5 → 4

Step 4: Merge them Alternately
Now we take one node from the First, then one node from the Second, and repeat.

Take 1 (First), point it to 5 (Second).
Take 5 (Second), point it to 2 (First's next).
Take 2 (First), point it to 4 (Second's next).
Take 4 (Second), point it to 3 (First's next).
Final result: 1 → 5 → 2 → 4 → 3 ✅


Explaination last loop with example:
First half: 1 → 2 → 3
Second half (reversed): 5 → 4

We have two pointers:
first is pointing to the head of the first half → node 1
second is pointing to the head of the reversed second half → node 5
Our goal is to weave them:
1 → 5 → 2 → 4 → 3

The Merge Loop (runs until second becomes empty)

Iteration 1
Before changing anything:
first = 1 → 2 → 3
second = 5 → 4

Step A: Save the "next" nodes (so we don't lose them)
tmp1 = first.next → tmp1 becomes node 2 (saves the rest of the first half).
tmp2 = second.next → tmp2 becomes node 4 (saves the rest of the second half).

Step B: Reorder the arrows
first.next = second → Make 1 point to 5.
Now the list looks like: 1 → 5 → 4 (but wait, we still have 2 and 3 saved in tmp1).
second.next = tmp1 → Make 5 point to 2.
Now the list looks like: 1 → 5 → 2 → 3.

Step C: Move the pointers forward for the next iteration
first = tmp1 → first now points to node 2.
second = tmp2 → second now points to node 4.

After Iteration 1, our pointers are:
first = 2 → 3
second = 4
The merged part so far: 1 → 5 → ... (and we still have 2 → 3 and 4 left to weave).

Iteration 2
Before changing anything:
first = 2 → 3
second = 4

Step A: Save the "next" nodes
tmp1 = first.next → tmp1 becomes node 3.
tmp2 = second.next → tmp2 becomes None (because 4 has no next).

Step B: Reorder the arrows
first.next = second → Make 2 point to 4.
Now the chain becomes: 2 → 4 (and since 2 was already pointed to by 5, the whole list now is 1→5→2→4).
second.next = tmp1 → Make 4 point to 3.
Now the whole list is: 1 → 5 → 2 → 4 → 3.

Step C: Move the pointers forward
first = tmp1 → first now points to node 3.
second = tmp2 → second now points to None.

Iteration 3 (Stop!)
Now we check the loop condition: while second:
Since second is now None (empty), the loop stops.
We don't need to do anything with node 3 because it's already the last node, and it correctly points to None.

Final Result
The list is now:
1 → 5 → 2 → 4 → 3
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    
        second = slow.next
        slow.next = None

        prev = None
        curr = second
        while curr:
            next_tmp = curr.next
            curr.next = prev
            prev = curr
            curr = next_tmp
        
        second = prev
        first = head

        while second:

            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2