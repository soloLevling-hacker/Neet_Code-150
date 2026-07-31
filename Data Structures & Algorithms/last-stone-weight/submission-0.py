'''
1. The Core Intuition
If you sort the array every time, it takes O(n² log n) or O(n²) time—which is terrible.
A Max-Heap gives you access to the heaviest stone in O(1) time and removes/inserts in O(log n) time, making the total solution O(n log n).

2. The Algorithm (Step-by-Step)
Build the Heap: Take all the stone weights and arrange them into a Max-Heap. (Note: Python's heapq is a Min-Heap by default, so we store negative values to simulate a Max-Heap).
Loop while more than 1 stone remains:
Pop the largest stone (x).
Pop the second largest stone (y).
If x == y: Both are destroyed (do nothing).
If x > y: The heavier crushes the lighter. The new stone weighs x - y. Push this new weight back into the heap.

Return the last remaining stone. If no stones are left, return 0.
'''

import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            haviest = -heapq.heappop(max_heap)
            second_haviest = -heapq.heappop(max_heap)

            if haviest > second_haviest:
                new_stone = haviest - second_haviest
                heapq.heappush(max_heap, -new_stone)

        return -max_heap[0] if max_heap else 0

'''
 Dry Run (Example: [2,7,4,1,8,1])
Expected output: 1

Heapify: [-8, -7, -4, -1, -2, -1] (Heaviest is 8).
Round 1: Pop 8 and 7. 8 > 7, new stone = 1. Heap now has [-4, -2, -1, -1, -1].
Round 2: Pop 4 and 2. 4 > 2, new stone = 2. Heap now has [-2, -1, -1, -1].
Round 3: Pop 2 and 1. 2 > 1, new stone = 1. Heap now has [-1, -1, -1].
Round 4: Pop 1 and 1. They are equal, both destroyed. Heap now has [-1].
Return: -(-1) = 1.

5. Time & Space Complexity
Time Complexity: O(n log n).
heapify costs O(n).
The loop runs at most n-1 times. Each heappop and heappush costs O(log n), so the loop costs O(n log n).
Space Complexity: O(n) for the heap array.
'''