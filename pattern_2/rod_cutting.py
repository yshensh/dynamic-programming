def solve_rod_cutting(lengths, prices, n):
    counter = len(lengths)
    # dp[i][j] represents the maximum prices of including ith rod given total length being j
    dp = [[0 for j in range(n+1)] for i in range(counter)]

    for index in range(counter):
        for current_length in range(1, n+1):
            include_current = prices[index] + dp[index][current_length-lengths[index]] if lengths[index] <= current_length else 0
            exclude_current = dp[index-1][current_length] if index > 0 else 0
            dp[index][current_length] =  max(include_current, exclude_current)

    return dp[counter-1][n]


def main():
  print(solve_rod_cutting([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))


main()
