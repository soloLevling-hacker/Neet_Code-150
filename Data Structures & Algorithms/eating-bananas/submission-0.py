'''
Ex:
piles = [3, 6, 7, 11]

That means:
Pile 1 has 3 bananas.
Pile 2 has 6 bananas.
Pile 3 has 7 bananas.
Pile 4 has 11 bananas.

Koko wants to eat all the bananas, but she has only h = 8 hours.
She decides on a speed (how many bananas she eats per hour).

But there are rules:
Each hour she can only work on one pile.
If the pile has fewer bananas than her speed, she eats all of that pile in that hour – she cannot "save" the leftover speed for another pile.

For example, if her speed is k = 5 bananas/hour:
Pile 3: she eats 3 (all), takes 1 hour. (She could eat 5, but there are only 3, so she finishes the pile.)
Pile 6: she eats 5 in the first hour, leaving 1, then in the second hour she eats that 1 (because the pile is now less than 5, she finishes it). So it takes 2 hours. (Total so far: 3 hours)
Pile 7: takes 2 hours (5 then 2).
Pile 11: takes 3 hours (5, 5, 1).
Total hours = 1 + 2 + 2 + 3 = 8. She exactly meets the 8‑hour limit.

If she chose k = 4, would it be possible? Let's check:
Pile 3: 1 hour (3 ≤ 4)
Pile 6: 2 hours (4 then 2)
Pile 7: 2 hours (4 then 3)
Pile 11: 3 hours (4, 4, 3)
Total = 1+2+2+3 = 8? Actually 1+2=3, +2=5, +3=8. Wait, that's also 8. So k=4 also works? Let's re‑calculate carefully:

Pile 3: 1 hour (she eats 3, pile empty, hour ends)
Pile 6: 1st hour: eats 4, leaves 2; 2nd hour: eats 2 (less than 4), pile empty → 2 hours.
Pile 7: 1st hour: eats 4, leaves 3; 2nd hour: eats 3 → 2 hours.
Pile 11: 1st: eats 4 (leaves 7); 2nd: eats 4 (leaves 3); 3rd: eats 3 → 3 hours.
Total = 1+2+2+3 = 8. So k=4 also works! But we are looking for the minimum speed, so maybe k=3?

Check k=3:
Pile 3: 1 hour (3)
Pile 6: 2 hours (3+3)
Pile 7: 3 hours (3+3+1) → actually 3,3,1 = 3 hours.
Pile 11: 4 hours (3+3+3+2)
Total = 1+2+3+4 = 10 hours > 8. So k=3 does not work.

So the answer for this example is 4? Wait, earlier we saw k=5 also works, but k=4 is smaller, and k=3 doesn't work, so the minimum is 4. But the problem's expected answer for [3,6,7,11], h=8 is actually 4? Let me confirm: I recall this problem from LeetCode #875, the answer for that exact input is 4. (Actually I remember it's 4? Let's see: if h=8, speed 4 gives 8 hours exactly, speed 5 gives 6 hours, speed 4 is the minimum. So yes, answer is 4.)
Now the code we have finds that minimum speed using a clever technique.

code explanation:

def minEatingSpeed(piles, h):
    def can_finish(k):
        hours = 0
        for pile in piles:
            hours += (pile + k - 1) // k   # ceil(pile / k)
            if hours > h:   # early exit optimization
                return False
        return True

can_finish is a nested function. It takes a speed k and returns True if total hours ≤ h.
hours accumulates.
For each pile, we add the ceil division.
If hours exceeds h early, we return False immediately (this saves time).
At the end, if we never exceeded, we return True.

    low, high = 1, max(piles)
Lowest possible speed is 1.

Highest possible speed is the largest pile.

    while low < high:
        mid = (low + high) // 2
        if can_finish(mid):
            high = mid   # try a smaller speed
        else:
            low = mid + 1   # need a faster speed
    return low

Binary search loop.
We check the middle speed.
If feasible, we move the upper bound down to mid (because mid could be the answer, but we want to see if an even smaller speed works).
If not feasible, we move the lower bound up to mid+1 (because mid is too slow, so answer must be larger).
When low == high, we've found the minimum feasible speed.

Note:
    Why not just use pile / k?
If you do pile / k in many languages, you get a decimal (like 7 / 3 = 2.333).
Then you'd have to call a math.ceil() function.
In the Koko problem, we must round up because if she has 7 bananas and eats 3 per hour:

Hour 1: eats 3 (left 4)
Hour 2: eats 3 (left 1)
Hour 3: eats 1 (finishes)

Even though she didn't eat a full 3 bananas in the last hour, it still took a full third hour. So 7 / 3 = 2.333, but we need the whole number 3.
The formula (pile + k - 1) // k gives us that 3 directly using only integer math.
'''

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(k):
            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k
                if hours > h:
                    return False
            return True
        
        low = 1
        high = max(piles)
        while low<high:
            mid = (low+high)//2

            if can_finish(mid):
                high = mid
            else:
                low = mid + 1
        return low



