def knapsack(weights, values, W):
    n = len(values)
    dp = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]

# Example usage:
values = [60, 100, 120]
weights = [10, 20, 30]
W = 50
print(f"Maximum value in Knapsack = {knapsack(weights, values, W)}")
