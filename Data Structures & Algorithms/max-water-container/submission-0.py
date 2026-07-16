'''
1. while left < right:
What: The main loop.
Why left < right: A container requires two distinct lines. If left meets or crosses right, there are no more pairs of walls to evaluate. We stop the search.

2. width = right - left
What: Calculates the horizontal distance between the two walls.
Physical Meaning: If left = 1 and right = 8, the width is 7. This is the base length of the rectangle that holds the water.

3. min_height = min(heights[left], heights[right])
What: Finds the shorter of the two walls.
Physical Meaning: Water overflows from the shorter wall. No matter how tall the other wall is, the water level cannot exceed the height of the shorter one. This is the limiting factor for the height of the container.

4. area = width * min_height
What: Calculates the water capacity for the current pair of walls using the rectangle area formula.
Physical Meaning: This is exactly how much water this specific pair of lines can hold.

5. max_area = max(max_area, area)
What: Compares the newly calculated area with the best area found in previous iterations.
Why: We keep the largest one, discarding the smaller.

6. if heights[left] < heights[right]:
What: The critical decision point. Checks which wall is the bottleneck (the shorter one).
The Intuition: The current area is completely capped by heights[left] (the left wall) because it is smaller. If we want to find a larger area, we must find a taller wall. But the width is going to shrink regardless of which pointer we move.

7. left += 1
What: Moves the left pointer one step to the right (discarding the current left wall).
The "Deep" Mathematical Proof (Why is it safe to discard?):
Let the current left be at index i and current right be at index j.
We know heights[i] < heights[j]. The area is heights[i] * (j - i).
Now, consider any other right wall k where i < k < j.
The new width (k - i) will be smaller than (j - i).
The new height will be min(heights[i], heights[k]). Because heights[i] is already smaller than heights[j], but we don't know about heights[k].
If heights[k] is taller than heights[i], the new height is still heights[i] (capped).
If heights[k] is shorter than heights[i], the new height is even less than heights[i].
Conclusion: In every scenario where we keep index i and move the right pointer inward, the Area will ALWAYS be less than or equal to heights[i] * (j - i).
Because the width shrinks, and the height can never exceed heights[i], index i can NEVER be part of a better solution. Therefore, we are mathematically justified in throwing it away forever by incrementing left.

8. else:
What: Executes if the left wall is not strictly smaller than the right wall (i.e., heights[left] >= heights[right]).

9. right -= 1
What: Moves the right pointer one step to the left (discarding the current right wall).
Symmetric Proof: The right wall is now the shorter one (or equal). Any container that keeps this right wall and moves the left wall inward will have a shorter width, and its height can never exceed heights[right]. Therefore, this right wall can never beat our current area, so we safely discard it and move right--.
(Note: If heights are equal, moving either pointer works. This code chooses to move the right one. The mathematical elimination holds for both).
'''

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        right =len(heights) - 1
        while left < right:
            width = right - left
            min_height = min(heights[left], heights[right])
            area = width * min_height
            max_area = max(max_area, area)

            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return max_area

                