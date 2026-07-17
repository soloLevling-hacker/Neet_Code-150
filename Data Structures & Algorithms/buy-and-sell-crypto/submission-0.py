'''
Line 1: Create a variable min_price and set it to a very large number (infinity). This will track the cheapest day to buy so far.

Line 2: Create a variable max_profit and set it to 0. This will track the best profit we have found so far.

Line 3: Start a loop that goes through every single price in the prices array, one by one, from left to right.

Line 4: Check if today's price is lower than our current min_price.
If Yes, we found a new cheaper buying day, so update min_price to today's price.

Line 5: Check if selling today would give us a better profit (price - min_price) than our current max_profit.
If Yes, update max_profit to this new higher profit.

Line 6: After checking all prices, return the final max_profit.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for p in prices:
            if p < min_price:
                min_price = p
            elif p - min_price > max_profit:
                max_profit = p - min_price
        return max_profit