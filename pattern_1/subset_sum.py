def can_partition(num, sum):
    n = len(num)
    # step 0: initialize dp[i][s]
    dp = [[False for s in range(sum+1)] for i in range(n)]

    # step 1: set initial values
    # '0' sum can always be found through an empty set
    for i in range(n):
        dp[i][0] = True
    # with only one number, we can form a subset only when the required sum is equal to its value
    for s in range(sum+1):
        dp[0][s] = True if num[0] == s else False
    
    # step 2: construct dp[i][s]
    # dp[i][s] is true if we can make sum 's' from the first 'i' numbers
    # 1) exclude the number num[i]
    #    check if we can get 's' from the subset excluding the number
    #    dp[i-1][s]
    # 2) include the number num[i]
    #    if num[i] is not more than 's'. we will check if we can find a subset
    #    to get the remaining sum dp[i-1][s-num[i]]
    for i in range(1, n):
        for s in range(1, sum+1):
            # exclude the number
            excluded_num = dp[i-1][s]
            # inlcude the number
            included_num = dp[i-1][s-num[i]] if num[i] <= s else False
            dp[i][s] = excluded_num | included_num
    return dp[n-1][sum]


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
  print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))


main()
