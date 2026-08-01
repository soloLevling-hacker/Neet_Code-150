from typing import List
from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.followee = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:

        user_check = [userId] + list(self.followee[userId])
        
        heap = []
        for user in user_check:
            if user in self.tweets and self.tweets[user]:
                tweet_list = self.tweets[user]
                last_idx = len(tweet_list) - 1
                timestamp, tweet_Id = self.tweets[user][last_idx] 
                heap.append((-timestamp, tweet_Id, user, last_idx))
        
        heapq.heapify(heap)
        
        result = []
        while heap and len(result)<10:
            neg_ts, tweet, user, idx = heapq.heappop(heap)
            result.append(tweet)

            if idx > 0:
                new_idx = idx - 1
                timestamp, tweet_Id = self.tweets[user][new_idx]
                heapq.heappush(heap, (-timestamp, tweet_Id, user, new_idx))
        return result 

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followee[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followee[followerId]:
            self.followee[followerId].discard(followeeId)

'''
    Core Approach: K-Way Merge using a Max-Heap:
The fundamental strategy is "Lazy K-Way Merge".
For a given user, the feed is composed of multiple sorted lists (each user’s own tweet timeline). Instead of merging all these lists entirely or sorting all tweets globally, we treat each user’s tweet list as a sorted stream (sorted by time, oldest to newest) and use a Max-Heap (implemented via negative timestamps) to pull the top 10 most recent tweets efficiently.

    The Intuition (Why this works):
Per-user sorting: Every user stores tweets in a list. Since postTweet appends new tweets at the end with an increasing timestamp, the last element in self.tweets[user] is always that user’s most recent tweet.

Global Top 10: The most recent tweet in the global feed must be the most recent tweet from one of the relevant users (you + your followees).

Heap for candidates: If we put the latest tweet of every relevant user into a heap, the root gives us the overall latest tweet.

Lazy pointer movement: When we pop that latest tweet (e.g., from User A), the next best candidate from User A is the tweet just before it (index idx - 1). We immediately push that older tweet into the heap. This way, the heap always contains exactly one "next best candidate" from each user.

Step-by-Step Algorithm for getNewsFeed
Identify Sources (user_check):
Combine the userId and all its followeeIds into a list.

Initialize the Heap:
Iterate over each source user.
If the user has tweets, get the last index (len(list) - 1).
Retrieve the timestamp and tweetId from that index.
Push (-timestamp, tweetId, user, index) into a list.
(We use negative timestamp because Python's heapq is a min-heap, but we want the largest timestamp at the top).

Heapify: Convert the list into a heap structure in O(U) time (where U is the number of relevant users).

Extract Top 10 (Merge Loop):
While result length is less than 10 and the heap is not empty:
Pop the root (-timestamp, tweet, user, idx).
Append tweet to result.

Crucial Step: Check if this user has an older tweet (i.e., if idx > 0).
If yes, fetch self.tweets[user][idx - 1] (the previous tweet).
Push (-new_timestamp, new_tweet, user, idx - 1) into the heap.

Return the result.

    Key Data Structures Used:
Data Structure	                        Purpose
self.time (int)	                        Global incrementing counter to ensure strictly chronological ordering across all users.
self.tweets (defaultdict(list))	        Stores the tweet history for every user. The list is implicitly sorted (oldest at index 0,  newest at index -1).
self.followee (defaultdict(set))	    Stores follow relationships. Using a set guarantees O(1) lookups for follow/unfollow and prevents duplicate entries.
heap (list of tuples)	                Acts as a max-heap. The tuple (-timestamp, tweetId, userId, index) allows us to lazily traverse each user's list backwards.

    Complexity Analysis:
Time Complexity:
Let U be the number of relevant users (1 user + their followees).
Building the heap costs O(U).
The loop runs at most 10 times. Each heappop and heappush costs O(log U).
Total: O(U + 10 log U). This is highly efficient because it does not depend on the total number of tweets.

Space Complexity:
O(U) for the heap, plus O(1) for the result (max size 10).

    Important Edge Cases Handled:
User has no tweets: The if user in self.tweets check skips them, preventing errors.
Self-follow prevention: follow() explicitly ignores followerId == followeeId.
Unfollowing a non-followed user: discard() safely ignores the operation without raising an error.
Less than 10 tweets available: The heap will empty naturally, returning whatever is available.

    Visual Summary (Mental Model):
Imagine 3 users (A, B, C) with their timelines (newest on the right):

A: [t1, t5, t9]
B: [t2, t7]
C: [t4, t6, t8, t10]

Initial Heap (takes the rightmost from each): [t9 (A), t7 (B), t10 (C)] → Pop t10 (C), push t8 (C).
Heap now: [t9 (A), t7 (B), t8 (C)] → Pop t9 (A), push t5 (A).
... and so on. This yields [t10, t9, t8, t7, t6, t5, t4, t2, t1] efficiently.
'''