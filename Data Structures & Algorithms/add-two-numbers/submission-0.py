'''
1. The Big Picture (The Math)
Remember how we add big numbers?

text
  3 4 2
+ 4 6 5
-------
  8 0 7

We start from the rightmost digit (units place): 2+5=7.
Then the tens place: 4+6=10, write 0, carry 1.
Then hundreds: 3+4+1=8.

Why are the lists reversed?
Because the linked list gives us the units place first!
342 is stored as 2 -> 4 -> 3 (head is the units place).
So we can just walk from the head (units) to the tail (hundreds) – exactly like doing math from right to left. No reversing needed!

2. The Train Analogy (Linked Lists)
ListNode: Each train car has a number (val) and a connector (next) to the next car.
l1 and l2 are the heads (first cars) of two trains carrying the digits.

3. Walking Through the Code Line-by-Line

dummy = ListNode(0)   # A fake starting car (value 0). 
current = dummy       # This points to the last car of our answer train.
carry = 0             # The extra "1" we bring to the next column.

Why a dummy node?
If we start with current = None, we'd have to write extra code to handle the very first digit. The dummy acts like a handle placed before our real answer. At the end, dummy.next perfectly points to the first real digit.

while l1 or l2 or carry:

We keep looping as long as:
There is a digit left in train 1 (l1), OR
There is a digit left in train 2 (l2), OR
We still have a carry (e.g., 5+5 = 10, we wrote 0, but still have a 1 to place).

    val1 = l1.val if l1 else 0
    val2 = l2.val if l2 else 0

If a train has run out of cars, we pretend it has a car with digit 0 (so adding 123 + 45 works fine).

    total = val1 + val2 + carry
    carry, digit = divmod(total, 10)

divmod(7, 10) → (0, 7) (7÷10 = 0 remainder 7)
divmod(10, 10) → (1, 0) (10÷10 = 1 remainder 0)
So carry gets the tens place, digit gets the ones place.

    current.next = ListNode(digit)
    current = current.next

We build our answer train car by car. Attach the new digit to current.next, then move current to that new car.

    if l1: l1 = l1.next
    if l2: l2 = l2.next

If the actual train still has cars, we move to the next one. If it was None (meaning we used the fake 0), we leave it as None.

return dummy.next

Skip the fake dummy car and give back the head of our answer train.

4. Step-by-Step Example: 342 + 465
Step	l1 (342)	l2 (465)	Carry (before)	Total (a+b+carry)	carry, digit    Answer Train so far
Start	2	        5       	0	            2+5+0 = 7	        (0, 7)	        7
Next	4	        6	        0	            4+6+0 = 10	        (1, 0)	        7 -> 0
Next	3	        4       	1	            3+4+1 = 8	        (0, 8)	        7 -> 0 -> 8
End	    None	    None	    0	            Stop	             -      	    Return 7->0->8
7->0->8 in reverse order means 807. And indeed, 342 + 465 = 807! ✅

5. What About Edge Cases? (Easy to understand)

Case 1: Different lengths
l1 = [1, 8] (81) and l2 = [0] (0).
Step 1: 1+0=1 → Answer [1]
Step 2: 8+0=8 → Answer [1, 8]
Result = 81. Perfect.

Case 2: Final carry-over
l1 = [5], l2 = [5] (5 + 5).
Step 1: 5+5=10 → digit=0, carry=1 → Answer [0]
Step 2: l1 and l2 are None, but carry is 1. Loop runs again: val1=0, val2=0, total=1 → digit=1, carry=0 → Answer [0, 1]
Result = 10. Correct!

Case 3: All zeros
[0] + [0] → total=0, digit=0, carry=0. Loop runs once, adds a 0, returns [0].

6. Summary for a Beginner
Why loops? To go digit by digit, just like column addition.
Why carry? Because 9+9 = 18, we write 8 and move the 1 to the next column.
Why dummy? So we don't stress about setting up the first node.
Why reversed lists? It makes life easier—the problem did the hard work for us by aligning the units place at the head!
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next