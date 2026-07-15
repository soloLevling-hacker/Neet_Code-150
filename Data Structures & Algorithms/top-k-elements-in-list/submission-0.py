'''
Line 1: count = Counter(nums)
What it does: Counter is a special dictionary from the collections module.
How it works: You give it a list, and it automatically counts how many times each element appears.
Example: If nums = [1,1,1,2,2,3], then count becomes {1: 3, 2: 2, 3: 1}.
Why: We need to know the frequency (how many times) before we can decide what is "Top K".

Line 2: buckets = [[] for _ in range(len(nums) + 1)]
What it does: Creates a list of empty lists.
How it works: If nums has 6 elements, this creates 7 empty buckets: [[], [], [], [], [], [], []].

The "Bucket Sort" Trick:
The index of this list represents the frequency.
Since a number can appear at most len(nums) times (e.g., if all numbers are the same), we need indices from 0 to len(nums). That's why we do + 1.
Index 0 will be ignored (no number appears 0 times).
Index 1 will hold numbers that appear once.
Index 3 will hold numbers that appear three times.

Line 3 & 4: for num, freq in count.items(): / buckets[freq].append(num)
What it does: Loops through our frequency dictionary.

How it works:
count.items() gives us (number, frequency) pairs (e.g., (1, 3), (2, 2), (3, 1)).
We grab the freq and use it as the index to put the num into the correct bucket.

Example:
num=1, freq=3 → Go to buckets[3] and append 1.
num=2, freq=2 → Go to buckets[2] and append 2.
num=3, freq=1 → Go to buckets[1] and append 3.
After this loop, buckets looks like:
[[], [3], [2], [1], [], [], []]
(Notice: Index 3 holds [1], index 2 holds [2], index 1 holds [3].)

Line 5: res = []
What it does: Creates an empty list where we will store our final answer (the top K frequent elements).

Line 6: for i in range(len(buckets) - 1, -1, -1):
What it does: This is a reverse loop.
How it works: range(start, stop, step). We start at the last index (highest frequency), go down to 0, stepping backwards (-1).
Why backwards? We want the most frequent numbers. The highest frequencies are at the end of the buckets list. So we grab the biggest indexes first.

Line 7: res.extend(buckets[i])
What it does: Takes everything inside buckets[i] and adds it to the end of our res list.

Why extend and not append?
append would put the whole list inside (e.g., [[1,2]]).
extend adds the individual numbers (e.g., [1, 2]). We want flat numbers.

Line 8 & 9: if len(res) >= k: return res[:k]
What it does: Checks if we have collected enough numbers to satisfy k.

How it works:
Imagine k = 2. We start from the highest bucket. We take all numbers from frequency 6, 5, 4... until we reach frequency 3.
At frequency 3, we add [1]. Our res is now [1]. Length is 1, which is not >= 2, so we keep going down.
Next, we go to frequency 2, we add [2]. Our res becomes [1, 2]. Length is 2, which is >= 2.
We immediately return res[:k] (which is [1, 2]).
Why res[:k]? Sometimes a bucket has more numbers than we need (e.g., frequency 2 has [4, 5] but we only need 1 more number to reach k). Slicing ensures we only give exactly k numbers and don't include extras.
'''

from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]

        for num, freq in count.items():
            bucket[freq].append(num)
         
        res = []
        for i in range(len(bucket)-1, -1, -1):
            res.extend(bucket[i])
            if len(res) >= k:
                return res[:k]

