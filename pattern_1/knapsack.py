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
    # 1) exclude the item at index 'i' +
    #    current_profit =  dp[i-1][c]
    # 2) include the item at index 'i' if its weight is not more than the capacity
    #    current_profit = profit[i] + dp[i-1][c-weight[i]]
    #    profit[i] => profit for item i
    #    dp[i-1][c-weight[i]] => profit from the remaining capacity and from remaining items
    
    # step 1: initialization
    # populate column where capacity = 0, with'0' capcity we have '0' profit
    for i in range(n):
        dp[i][0] = 0

    # populate row where item index = 0
    # if there is only one item, it will be taken as long as it is not more than than the capacity
    for c in range(1, capacity+1):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    # step 2: populate dp[i][c]
    for i in range(1, n):
        for c in range(1, capacity+1):
            # exclude item[i]    
            excluded_profits = dp[i-1][c]
            # include item[i]
            included_profits = profits[i] + dp[i-1][c-weights[i]] if weights[i] <= c else 0
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
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()
