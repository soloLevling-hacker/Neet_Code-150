'''
Problem:
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:
TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

Example 1:
Input:
["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1], "get", ["alice", 2], "set", ["alice", "sad", 3], "get", ["alice", 3]]
Output:
[null, null, "happy", "happy", null, "sad"]


Explanation:

Data Structure:
self.store is a dictionary (hash map).
Each key maps to a list of pairs (timestamp, value).
For example: {"foo": [(1, "bar"), (4, "bar2"), (7, "baz")]}
The problem guarantees that for the same key, set calls are made with strictly increasing timestamps, so the lists are always sorted by timestamp.

set(key, value, timestamp)
if key not in self.store:
    self.store[key] = []
self.store[key].append((timestamp, value))

If the key doesn’t exist, create a new empty list.
Append the new (timestamp, value) tuple to the list.
Because timestamps are strictly increasing, the list remains sorted without needing extra work.
Time complexity: O(1) amortised (appending to a list).

get(key, timestamp)
if key not in self.store:
    return ""
pairs = self.store[key]
lo, hi = 0, len(pairs) - 1
ans = ""
while lo <= hi:
    mid = (lo + hi) // 2
    if pairs[mid][0] <= timestamp:
        ans = pairs[mid][1]   # this candidate is valid, but there might be a later one
        lo = mid + 1          # search in the right half
    else:
        hi = mid - 1          # search in the left half
return ans

Step‑by‑step:
Key existence check – if the key is not in the store, return "".
Retrieve the list of (timestamp, value) for that key.
Binary search over the list (which is sorted by timestamp) to find the rightmost entry with timestamp ≤ the given timestamp.
Initialize lo = 0, hi = len(pairs) - 1, and ans = "".

While lo <= hi:
Compute mid = (lo + hi) // 2.

Compare pairs[mid][0] (the timestamp at mid) with the requested timestamp:
If it’s ≤ the requested timestamp, it’s a valid candidate. Store its value in ans, and move lo = mid + 1 to see if there is a later valid entry (larger timestamp still ≤ requested).
Otherwise, the mid timestamp is too large, so move hi = mid - 1 to search the left (earlier) half.
After the loop, ans holds the value of the latest valid timestamp (or "" if none were found).

Why binary search works?
Because the list is sorted by timestamp, we can efficiently find the rightmost element ≤ target in O(log n) time, where n is the number of entries for that key.

Edge cases handled:
Key doesn’t exist → returns "".
All stored timestamps are > requested timestamp → the binary search will never find a valid mid, so ans stays "" and is returned.
The requested timestamp matches exactly one of the stored timestamps → that entry is found, and because we search to the right, we may also find later entries if they have the same timestamp? (But timestamps are strictly increasing, so no duplicates; even if there were, we’d return the rightmost one, which is fine.)

Complexity Summary
set: O(1) amortised.
get: O(log n) for that key’s list.
Space: O(total number of stored entries).
'''

class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.store:
            return ""
        paires = self.store[key]
        left = 0
        right = len(paires) - 1
        ans = ''
        while left <= right:

            mid = (left+right)//2
            if paires[mid][0] <= timestamp:
                ans = paires[mid][1]
                left += 1
            else:
                right -= 1
        return ans





