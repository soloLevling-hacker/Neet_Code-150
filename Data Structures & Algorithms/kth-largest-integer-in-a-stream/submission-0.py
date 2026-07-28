'''
Design a class KthLargest to find the k‑th largest element in a stream of numbers.

Constructor: KthLargest(int k, int[] nums) – initialises the object with the integer k and the initial stream of integers nums.
Method: int add(int val) – appends val to the stream and returns the element representing the k‑th largest element in the current stream.

    Key Insight:
The k‑th largest element in a collection is the minimum element among the k largest elements.
If we maintain a min‑heap of exactly the k largest elements seen so far:
The root (smallest) of that heap is automatically the k‑th largest overall.

    When a new number arrives:
Add it to the heap.
If the heap size exceeds k, pop the smallest element (which is now the (k+1)‑th largest, no longer needed).
The heap always contains the top k elements, and heap[0] gives the answer in O(1).

    Approach:
Initialisation:
Store k as an instance variable.
Create an empty min‑heap.
Push all elements from nums into the heap.
While heap.size() > k, remove the smallest element.

Add operation:
Push the new value val into the heap.
If heap.size() > k, pop the smallest element.
Return heap[0] (the root), which is the k‑th largest.
'''


import heapq
from typing import List
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]


'''
    Example Walkthrough:
Let k = 3 and initial nums = [4, 5, 8, 2].

Initialisation:
Heap = []
add 4 → heap = [4] (size 1 ≤ 3)
add 5 → heap = [4, 5]
add 8 → heap = [4, 5, 8]
add 2 → heap = [2, 4, 5, 8] (size 4 > 3) → pop 2 → heap = [4, 5, 8]

k‑th largest (3rd largest) = 4 (numbers: 8, 5, 4).

Stream operations:
add(val)	Heap (size 3)	                                    Return (heap[0])	Explanation
add(3)	    [4, 5, 8] → push 3 → [3,4,5,8] → pop 3 → [4,5,8]	    4	             3 is smaller than all, so it's removed. 4 remains 3rd largest.
add(5)	    [4,5,8] → push 5 → [4,5,5,8] → pop 4 → [5,5,8]      	5	             Now the 3 largest are 8,5,5 → 3rd largest is 5.
add(10)	    [5,5,8] → push 10 → [5,5,8,10] → pop 5 → [5,8,10]	    5	             3 largest are 10,8,5 → 3rd largest is 5.
add(9)	    [5,8,10] → push 9 → [5,8,9,10] → pop 5 → [8,9,10]	    8	             3 largest are 10,9,8 → 8.
add(4)	    [8,9,10] → push 4 → [4,8,9,10] → pop 4 → [8,9,10]	    8	             4 is smaller, removed.

    Complexity:
Time per add(): O(log k) – each heap operation (push/pop) takes logarithmic time in the heap size.
Space: O(k) – the heap stores at most k elements.

    Important Notes:
If nums has fewer than k elements initially, the heap size will be less than k. The method add will still work correctly; it will return the smallest element present until we have seen at least k numbers.
This is a classic problem that demonstrates the power of min‑heap for tracking top‑k elements efficiently. An alternative using a max‑heap of the rest + a min‑heap for the k largest is also possible but unnecessarily complex for this use case.
The solution is stream‑friendly – it processes each element in O(log k) and does not require storing the entire history.
'''
