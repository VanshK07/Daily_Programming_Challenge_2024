import math

def coin_change(coins, amount):
    dp = [math.inf] * (amount + 1)
    
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != math.inf else -1

coins = [1, 2, 5]
amount = 11
result = coin_change(coins, amount)
print(f"The minimum number of coins needed: {result}")
