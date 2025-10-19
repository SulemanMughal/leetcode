# Ref : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/



# ⏱️ Complexity
# Time: O(n) — one pass
# Space: O(1) — constant extra space

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(1, len(prices)):

            # It accumulates profit for every price increase, simulating buying before every rise and selling at the peak, to maximize total profit.
            # This condition checks if today’s price (prices[i]) is higher than yesterday’s price (prices[i - 1]).
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit
        