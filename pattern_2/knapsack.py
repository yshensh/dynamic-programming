def solve_knapsack(profits, weights, capacity):
    dp = solve_knapsack_dp(profits, weights, capacity)
    print_selected_elements_dp(dp, profits, weights, capacity)
    return dp[len(profits)-1][capacity]


def solve_knapsack_dp(profits, weights, capacity):
    # basic checks
    n = len(profits)
    if capacity <=0 or n == 0 or len(weights) != n:
        return 0
    
    # step 0: initialize dp[i][c] which represents the maximum knapsack profit for capcity 'c' calculated from the first 'i' items
    dp = [[0 for c in range(capacity+1)] for i in range(n)]
    
    # for each item in index 'i' and capacity 'c'
    # 1) exclude the item at index 'i'
    #    current_profit =  dp[i-1][c]
    # 2) include the item at index 'i' if its weight is not more than the capacity
    #    current_profit = profit[i] + dp[i][c-weight[i]]
    #    profit[i] => profit for item i
    #    dp[i-1][c-weight[i]] => profit from the remaining capacity and from remaining items
    
    # step 1: initialization
    # populate column where capacity = 0, with'0' capcity we have '0' profit
    for i in range(n):
        dp[i][0] = 0

    # don't need to populate row where item index = 0 for unbounded knapsack

    # step 2: populate dp[i][c]
    for i in range(n):
        for c in range(1, capacity+1):
            # exclude item[i]    
            excluded_profits = dp[i-1][c] if i > 0 else 0
            # include item[i] 
            # (unbounded knapack: we use dp[i][c-weights[i]];
            #  0/1 knapsack: we use dp[i-1][c-weights[i])
            included_profits = profits[i] + dp[i][c-weights[i]] if weights[i] <= c else 0
            # take the maximum
            dp[i][c] = max(excluded_profits, included_profits)
    return dp


# traverse dp from the last item. 
# if we skip an item, then we take the profit from the remaining items (from the cell right above dp[i-1][c])
# if we include the item, then we jump to the reamining profit to find more items
def print_selected_elements_dp(dp, profits, weights, capacity):
    n = len(profits)
    total_profits = dp[n-1][capacity]
    print("selected items and weights:")
    for i in range (n-1, 0, -1):
        if total_profits != dp[i-1][capacity]:
            print(f'item: {i}, weights: {weights[i]}, profits: {profits[i]}')
            capacity -= weights[i]
            total_profits -= profits[i]
    if total_profits != 0:
        print(f'item: 0, weights: {weights[0]}, profits: {profits[0]}')


def main():
  print(solve_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 8))
  print(solve_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 6))


main()
