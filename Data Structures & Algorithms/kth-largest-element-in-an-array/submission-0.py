'''
Find the Kth largest element in an unsorted array. (e.g., [3,2,1,5,6,4], k=2 → Output: 5)

The Golden Rule (Recap)
In K Closest, we wanted the K smallest distances → We used a Max-Heap of size K.
In Kth Largest, we want the Kth largest (which means we want to keep the K biggest numbers) → We use a Min-Heap of size K.

Why?
We push numbers into a Min-Heap. As soon as the size exceeds K, we pop the smallest number (the root). By the end, the heap contains the K largest numbers, and the root of the heap is the smallest among them—which is exactly the Kth largest overall!

NOTES:

The Ultimate Cheat Sheet (Memorize This!)

Problem	Goal	        Heap Type	                        Heap Size	Action on overflow
K Closest Points	    Keep smallest distances	Max-Heap	K	        Pop the largest (root)
Kth Largest Element	    Keep largest numbers	Min-Heap	K	        Pop the smallest (root)
Last Stone Weight	    Smash heaviest two	Max-Heap	    N(all)  	N/A (pop two at a time)
Merge K Lists	        Get smallest head	Min-Heap	    K	        N/A (pop one, push next)
'''

import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        min_heap = []

        for num in nums:

            heapq.heappush(min_heap, num)

            if len(min_heap)>k:
                heapq.heappop(min_heap)

        return min_heap[0]

'''
    Dry Run: nums = [3,2,1,5,6,4], k=2
Push 3,2,1 (size=3 > 2 → pop 1). Heap = [2,3].
Push 5 (pop 2). Heap = [3,5].
Push 6 (pop 3). Heap = [5,6].
Push 4 (pop 4? Wait, heap is [5,6]. Push 4 → [4,5,6], size=3 > 2 → pop 4). Heap = [5,6].
Root 5 is returned. Correct!

Complexity: O(N log K) time, O(K) space.
'''

#ANOTHER

'''
Problem 2: Merge K Sorted Lists (Quick Version)
You have K sorted linked lists. Merge them into one sorted list.

    Intuition:
You always need to pick the smallest node among the heads of all K lists. A Min-Heap is perfect here.
Push the head of every non-empty list into a Min-Heap (store (node.val, index, node) to handle comparisons).
Pop the smallest node, append it to the result, and push its next node back into the heap.
Repeat until the heap is empty.

    Python Code (Conceptual):
import heapq

class Solution:
    def mergeKLists(self, lists):
        min_heap = []
        # Push the head of each list
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        
        dummy = ListNode(0)
        curr = dummy
        
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
        
        return dummy.next
Complexity: O(N log K) time (where N is total nodes), O(K) space.
'''