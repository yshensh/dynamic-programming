import math

def count_change(denominations, total):
    n = len(denominations)

    # initialize dp[i][t], which represents the minimum of coins needed to sum up to t given coin[i]
    dp = [[math.inf for t in range(total+1)] for i in range(n)]

    # initialize value for dp[i][0]
    for i in range(n):
        dp[i][0] = 0

    # construct dp[i][t]
    for i in range(n):
        for t in range(1, total+1):
            include_coin = 1 + dp[i][t - denominations[i]] if (t >= denominations[i]) else math.inf
            exclude_coin = dp[i-1][t]
            dp[i][t] = min(include_coin, exclude_coin)

    return -1 if dp[n-1][total] == math.inf else dp[n-1][total]
        
    
def main():
  print(count_change([1, 2, 3], 5))
  print(count_change([1, 2, 3], 11))
  print(count_change([1, 2, 3], 7))
  print(count_change([3, 5], 7))


main()
