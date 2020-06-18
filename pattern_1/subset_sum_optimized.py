def can_partition(num, sum):
    n = len(num)
    # step 0: initialize dp[s]
    dp = [False for s in range(sum+1)]

    # step 1: set initial values
    # '0' sum can always be found through an empty set
    dp[0] = True
    # if we have only one number, we can have a subset only when the required sum is equal to its value
    for s in range(0, sum+1):
        dp[s] = True if num[0] == s else False

    # step 2: process all sub-arrays for all sums
    for i in range(1, n):
        for s in range(sum, -1, -1):
            # exclude the number
            excluded_num = dp[s]
            # inlcude the number
            included_num = dp[s-num[i]] if num[i] <= s else False
            dp[s] = excluded_num | included_num
    return dp[sum]


def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
  print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))


main()
