'''
1. The Core Intuition
You have N points. You need the K smallest distances.
If you use a Min-Heap and push all N points, you use O(N) memory and O(N log N) time—that's just sorting with extra steps.

The optimized trick: Use a Max-Heap of size exactly K.
As you iterate through the points, push them into the heap.
If the heap size exceeds K, pop the largest distance (the root of the Max-Heap).
By the end, your heap contains only the K smallest distances! This runs in O(N log K) time and O(K) memory.

2. The Algorithm (Step-by-Step)
Initialize an empty Max-Heap. (Note: Python's heapq is a Min-Heap, so to make a Max-Heap, we store the negative distance).

Iterate through every point (x, y):
Calculate the squared distance: dist = x*x + y*y. (We use squared distance to avoid floating-point decimals and slow sqrt() calls).
Push (-dist, x, y) onto the heap.
If len(heap) > K: pop the root. This removes the point with the largest distance (because negative distance makes the largest positive distance the smallest negative number, so it sits at the root).

Return the (x, y) pairs left in the heap.

NOTE:
To find the K smallest items, use a Max-Heap of size K.
To find the K largest items, use a Min-Heap of size K.
'''

import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        max_heap = []

        for x, y in points:
            dist = x*x + y*y

            heapq.heappush(max_heap, (-dist, x, y))

            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return [[x,y] for (_, x, y) in max_heap]

'''
    Dry Run (Example: points = [[1,3], [-2,2], [5,8], [0,1]], k = 2)
Point 1 (1,3): dist = 10. Heap = [(-10, 1, 3)]. (Size 1 ≤ K)
Point 2 (-2,2): dist = 8. Heap = [(-10,1,3), (-8,-2,2)]. (Size 2 ≤ K)
Point 3 (5,8): dist = 89. Push -> Heap = [(-89,5,8), (-10,1,3), (-8,-2,2)]. Size = 3 > K. heappop() removes -89 (which is the smallest negative, meaning the largest positive distance). Heap is back to [(-10,1,3), (-8,-2,2)].
Point 4 (0,1): dist = 1. Push -> Heap = [(-10,1,3), (-8,-2,2), (-1,0,1)]. Size = 3 > K. heappop() removes -10 (distance 10). Heap left = [(-8,-2,2), (-1,0,1)].
Return: [[-2,2], [0,1]]. Correct! (Distances 8 and 1 are the two smallest).

    Time & Space Complexity
Time Complexity: O(N log K).

We iterate through all N points. Each heappush and heappop takes O(log K) because the heap size never exceeds K.

Space Complexity: O(K) for the heap. (Plus O(1) output space, not counting the return array)
'''