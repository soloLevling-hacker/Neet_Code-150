'''
It looks simple (just schedule tasks with a cooldown), but it forces you to combine a Max-Heap (to always pick the most frequent task) with a Queue (to track the cooldown timer).

Here is the complete breakdown of the optimal greedy solution.

    1. The Core Intuition
You have tasks [A,A,A,B,B,B] and cooldown n = 2.
You cannot do A again for 2 cycles. To minimize idle time, you must always execute the task with the highest remaining frequency first.

If you do A (count 3), then B (count 3), then A is still on cooldown, so you must idle.
If you did A, then B, then A is ready again, but A is still frequent, so you do it.

The trick is tracking when a task becomes available again.

    2. The Algorithm (Max-Heap + Cooldown Queue)
We use two data structures:

Max-Heap: Stores (-remaining_count, task_id). Always gives us the task with the most remaining copies.

FIFO Queue (or list with time stamps): Stores tasks that are currently "cooling down". We pop them from the heap, push them into the queue with a timestamp of when they can be used again.

Step-by-Step:
Count frequencies of all tasks using a HashMap.
Push all negative frequencies into a Max-Heap.
Initialize time = 0.

Loop while the heap is not empty OR the cooldown queue is not empty:
Increment time += 1.

If heap is not empty: Pop the most frequent task (count). Decrease its count by 1 (since we just executed it). If the remaining count is still > 0, push it into a cooldown queue with available_time = time + n (it cannot be used again until this time).

Check the queue: Look at the front of the queue. If its available_time == time, it means the cooldown is over! Pop it from the queue and push it back onto the heap.

(If the heap is empty, it means we are forced to idle. We still increment time and check the queue).
'''

from typing import List
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        if n == 0:
            return len(tasks)
        count = Counter(tasks).values()
        max_heap = [-cnt for cnt in count]
        heapq.heapify(max_heap)

        cooldown_queue = deque()
        time = 0

        while max_heap or cooldown_queue:

            time += 1

            if max_heap:
                cnt = -heapq.heappop(max_heap)
                cnt -= 1

                if cnt > 0:
                    cooldown_queue.append((cnt, time+n))
            
            if cooldown_queue and cooldown_queue[0][1] == time:
                cnt, _ = cooldown_queue.popleft()
                heapq.heappush(max_heap, -cnt)

        return time