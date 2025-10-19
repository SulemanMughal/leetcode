# Ref : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/



def maxProfit(prices):
    """
    Time: O(n)
    Space: O(1)
    """

    # It efficiently finds the best buy/sell days for maximum profit in one pass.
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
    return max_profit

