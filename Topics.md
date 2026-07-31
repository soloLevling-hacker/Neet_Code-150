**HEAP/PRIORITY QUEUE**

1. The Two Golden Rules of a Heap
For a binary heap (the most common type), it must obey both of these rules:

Shape Property (Complete Tree): It must be a complete binary tree. This means every level is completely filled except possibly the last, and the last level is filled from left to right. (No gaps on the left side!).
Order Property (Heap Property): Every parent node must be ordered relative to its children. This creates two types:
Max-Heap: The value of every parent node is greater than or equal to the values of its children. (The root holds the maximum element).
Min-Heap: The value of every parent node is less than or equal to the values of its children. (The root holds the minimum element).

2. How is it stored in memory?
Even though a heap is a tree, it is almost always implemented using an array (not linked nodes like a BST).

Because it is a complete tree, you can map it to an array with simple math:
Root is at index 0.
For any node at index i:
Left Child index = 2*i + 1
Right Child index = 2*i + 2
Parent index = (i - 1) / 2 (integer division)
This array representation makes heaps incredibly memory-efficient (no pointers needed).

3. Core Operations and Time Complexities
Heaps are famous for their speed in finding the max/min element.

Operation	                Description	                                                                                  Time Complexity
Peek (Find Max/Min)      	Look at the root element.	                                                                    O(1)

Insert (Push)	            Add a new element to the end (bottom-left), then "bubble it up" by swapping with its          O(log n)
                          parent until the heap property is restored.	

Extract (Pop)	            Remove the root (max/min). Replace it with the last element in the array, then                O(log n)
                          "bubble it down" (heapify) by swapping with the larger/smaller child until the
                          property is restored.	

Heapify	                  Build a heap from an unsorted array of n elements by calling bubble-down on                    O(n) (Surprisingly, not O(n log n)!)
                          internal nodes.	

4. Where are Heaps used? (Real-world Applications)
Priority Queues: The backbone of operating system task scheduling (the highest priority process runs first) and event-driven simulations.

Dijkstra's Algorithm: Used to find the shortest path in graphs by efficiently extracting the node with the smallest distance.
Prim's Algorithm: Used to find Minimum Spanning Trees in networks.
Heap Sort: An in-place, comparison-based sorting algorithm that runs in O(n log n) (and is often faster than Quicksort in worst-case scenarios).
Finding K-th Smallest/Largest: If you need the top 10 largest items in a billion-item list, you use a Min-Heap of size 10.

5. Important Distinction: Heap vs. Binary Search Tree (BST)
This is a common interview pitfall:
BST: Left child < Parent < Right child. Used for searching (O(log n)).
Heap: Parent > (or <) both children. No strict ordering between left and right siblings. Used for prioritizing (O(1) to find the extreme value).

6. Variations of Heaps
Binary Heap: The standard one described above (2 children per node).
Binomial Heap / Fibonacci Heap: More complex structures used in advanced graph algorithms. They offer better amortized runtimes for certain operations (like O(1) for decrease-key in Fibonacci heaps).
D-ary Heap: A heap where each node has d children (used in Dijkstra's for dense graphs).

Quick Visual Example (Min-Heap)
If you insert 10, 20, 15, 30, 40 into a Min-Heap, the array will look like [10, 20, 15, 30, 40].
Visualized as a tree:
       10      <-- Root (Smallest)
      /  \
     20   15   <-- Both are > 10
    /  \
   30   40     <-- Both are > 20
If you pop() the root (10), the algorithm replaces it with 40, then swaps it down until the structure is valid again, resulting in [15, 20, 40, 30].

