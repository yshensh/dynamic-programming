def find_max_steal(wealth):
    # initialize dp[]
    n = len(wealth)
    dp = [0 for i in range(n+1)]

    # base case
    dp[0] = 0
    dp[1] = wealth[0]

    # deductive case:  every dp[i] is the ith step (which is the minimum of the two recursive calls). 
    # 1) steal from current house and skip one to steal next: wealth[i] + dp[i-1]
    # 2) skip current house to steel from the adjacent house: 
    for i in range(1, n):
        dp[i + 1] = max(wealth[i] + dp[i-1],
                        dp[i]) 

    return dp[n]

def main():
    print(find_max_steal([2, 5, 1, 3, 6, 2, 4]))
    print(find_max_steal([2, 10, 14, 8, 1]))


main()