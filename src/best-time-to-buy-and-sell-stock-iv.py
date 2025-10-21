# Ref : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/submissions/1806179131/


# ⏱️ Time and Space Complexity
# Time	O(k × n)
# Space	O(k × n) (can be optimized to O(n))

def maxProfit(k: int, prices: list[int]) -> int:
    n = len(prices)
    if n == 0:
        return 0
    

    # If k is large enough, behave like unlimited transactions
    # When k ≥ n // 2, the transaction limit doesn't matter, so we switch to a faster O(n) greedy algorithm to save time and space.
    if k >= n // 2:
        profit = 0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

    # dp[t][i] stores the max profit at day i with at most t transactions, allowing us to build up the solution iteratively. The final answer is dp[k][n-1] (max profit with k transactions by the last day).
    dp = [[0] * n for _ in range(k + 1)]


    # For each transaction, for each day, you decide whether to sell or not.
    # max_diff helps you quickly compute the best buy/sell combination for each transaction.
    # The result is the maximum profit with at most k transactions, 
    for t in range(1, k + 1):
        max_diff = -prices[0]
        for i in range(1, n):
            dp[t][i] = max(dp[t][i - 1], prices[i] + max_diff)
            max_diff = max(max_diff, dp[t - 1][i] - prices[i])

    return dp[k][-1]
