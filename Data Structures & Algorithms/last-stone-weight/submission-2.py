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

#Another

'''
The Bucket Sort Algorithm (Step-by-Step)
Instead of dynamically sorting, we create an array buckets of size 1001 (index 0 to 1000).
buckets[w] stores the count of how many stones weigh exactly w.
Count all the stones in the buckets array.
Find the heaviest: Start a pointer max_weight at 1000 and walk it downwards until you find a bucket with a count > 0.

The Smash Loop:
Find the heaviest stone (x) by moving max_weight down to the next non-zero bucket.
Find the second heaviest (y) by moving max_weight down again to the next non-zero bucket (or the same bucket if there are at least 2 stones of that weight).

Smash them:
Decrease the count of x and y by 1.
If x > y, calculate new_weight = x - y, and increment buckets[new_weight] by 1.
Crucial optimization: If new_weight > max_weight, update max_weight = new_weight (because the new stone might be heavier than the current pointer).
Return: When the loop ends, walk max_weight down to find the last remaining stone. Return that index.

Python Code (Optimized Bucket Sort)
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Constraint: 1 <= stones[i] <= 1000
        MAX_WEIGHT = 1000
        buckets = [0] * (MAX_WEIGHT + 1)
        
        # Step 1: Count all stones
        for weight in stones:
            buckets[weight] += 1
            
        # Step 2: Set pointer to the maximum possible weight
        max_weight = MAX_WEIGHT
        
        # Step 3: Smash stones
        while max_weight > 0:
            # Skip empty buckets to find the heaviest stone
            while max_weight > 0 and buckets[max_weight] == 0:
                max_weight -= 1
            
            if max_weight == 0:
                break  # No stones left
                
            # We found the heaviest stone (x)
            # Decrease its count by 1 (we are taking it)
            buckets[max_weight] -= 1
            heaviest = max_weight
            
            # Now find the second heaviest (y)
            # We start searching from 'heaviest' downwards
            second_heaviest = heaviest
            while second_heaviest > 0 and buckets[second_heaviest] == 0:
                second_heaviest -= 1
            
            # If no second stone exists, we are done (the heaviest is the last one)
            if second_heaviest == 0 and buckets[0] == 0:
                # Put the heaviest back, it's the only one left
                buckets[heaviest] += 1
                break
                
            # Take the second heaviest
            buckets[second_heaviest] -= 1
            
            # Smash them!
            if heaviest > second_heaviest:
                new_stone = heaviest - second_heaviest
                buckets[new_stone] += 1
                # Optimize: move max_weight up if the new stone is heavier
                if new_stone > max_weight:
                    max_weight = new_stone
            # else (heaviest == second_heaviest): both destroyed, do nothing.

        # Step 4: Find the final remaining stone
        while max_weight > 0 and buckets[max_weight] == 0:
            max_weight -= 1
            
        return max_weight

Dry Run with [2,7,4,1,8,1]
Buckets: buckets[1]=2, [2]=1, [4]=1, [7]=1, [8]=1. max_weight = 8.

Loop 1: Find 8 (take it). Find 7 (take it). Smash -> 8-7=1. buckets[1] becomes 3. max_weight stays 8 (bucket 8 is now 0, but we'll skip it next).
Loop 2: Skip 8, find 4 (take it). Skip 3, find 2 (take it). Smash -> 4-2=2. buckets[2] becomes 1.
Loop 3: Skip 4,3. Find 2 (take it). Skip 1... wait, buckets[1] is 3! Find second = 1 (take it). Smash -> 2-1=1. buckets[1] stays 2 (was 3, took 1, added 1 = still 3? Let's count: originally 3, take one for second=2 left, add new=1 -> 3 total).
Loop 4: Find 1 (take it). Find second 1 (take it). Smash -> equal, both destroyed. buckets[1] goes from 3 to 1.
Loop 5: Find 1 (take it). No second stone found. Break and put it back.
Return: max_weight = 1. Correct!

Heap vs. Bucket Sort: Which is better?
Feature	                Max-Heap Solution	                        Bucket Sort Solution
Time Complexity	        O(n log n)	                                O(n + W) (Where W = max weight, i.e., 1000)
Space Complexity	    O(n)	                                    O(W) (Constant, ~1001)

Scalability	            Scales to any integer size.	                Only works if max weight is known and small.
Interview Expectation	Tests your knowledge of Priority Queues.	Tests your ability to spot constraints and optimize.

Which one should you use in an interview?
Start with the Heap. It's the universal, "textbook" answer that works for any input.
Then mention the Bucket Sort as a bonus exactly like this:
"Given the constraint that weights max out at 1000, we could actually optimize this to O(n) using a counting array. However, if the weights were massive or unknown, the heap is the safer, more scalable choice."
'''