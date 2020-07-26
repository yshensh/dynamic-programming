def count_change(denominations, total):
    # dp[i][t] stores the all possible sums (the total number of distinct ways to make up that amount) for every possible total t and for every combination of coins; in other words, given coin[i] (a.k.a denominations[i])), how many ways are there to make up sum 't'?

    # total number of coins
    n = len(denominations)

    # initial construction of dp[i][t]
    dp = [[0 for t in range(total+1)] for i in range(n)]

    # for t = 0, which means to find number of ways to make up sum 0. Given any coin, '0' total can always be found through an empty set. So dp[i][0] = 1
    for i in range(n):
        dp[i][0] = 1

    # construct dp[i][t]
    for i in range(n):
        for t in range(1, total+1):
            exlcude_coin = dp[i-1][t] if i >= 1 else 0
            include_coin = dp[i][t-denominations[i]] if t >= denominations[i] else 0
            dp[i][t] = exlcude_coin + include_coin
    
    return dp[n-1][total]

def main():
    print(count_change([1, 2, 3], 5))

main()
