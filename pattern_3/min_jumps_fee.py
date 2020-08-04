def find_min_fee(fee):
    # initialize dp[]
    n = len(fee)
    dp = [0 for x in range(n+1)]

    # base case
    dp[0] = 0
    dp[1] = fee[0]
    dp[2] = fee[0]

    # deductive case:  every dp[i] is the ith step (which is the minimum of the three recursive calls. 
    # when i = 0, 0 step taken
    # when i = n-1, reaches top (we get dp[n])
    # start from fee[2]
    # if we take 1 step from i to reach to i+1, the total cost is fee[i] + dp[i] 
    # if we take 2 step from i-1 to reach to i+1, the total cost is fee[i-1] + dp[i-1] 
    # if we take 3 step from i-2 to reach to i+1, the total cost is fee[i-2] + dp[i-2] 
    for i in range(2, n):
        dp[i + 1] = min(fee[i] + dp[i], # take +1 step to reach to i+1
                        fee[i - 1] + dp[i - 1], # take +2 steps to reach to i+1
                        fee[i - 2] + dp[i - 2]) # take +3 steps to reach to i+1

    return dp[n]


def main():

  print(find_min_fee([1, 2, 5, 2, 1, 2]))
  print(find_min_fee([2, 3, 4, 5]))


main()
