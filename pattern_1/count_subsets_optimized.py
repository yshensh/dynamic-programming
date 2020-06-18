def count_subsets(num, sum):
    # basic checks
    n = len(num)
    if n == 0:
        return 0
    
    # step 0: initialize dp[s] which represents all possible sums with every subset
    dp = [0 for s in range(sum+1)]
    
    # for each item in index 'i' and sum 's'
    # 1) exclude the number at index 'i'
    #    dp[s] => count all the subsets without the given number up to the given sum
    # 2) include the number at index 'i' if its value is not more than the 'sum'. 
    #    dp[s-num[i]] => count all the subsets to get the remaining sum (s-num[i])
    
    # step 1: initialization
    # '0' sum can always be found through an empty set
    for i in range(n):
        dp[0] = 1

    # populate row where item index = 0
    # with only one number, we can form a subset only when the required sum is equal to the number
    for s in range(1, sum+1):
        dp[s] = 1 if num[0] == s else 0            

    # step 2: populate dp[s]
    for i in range(1, n):
        for s in range(sum, -1 , -1):
            # exclude item[i]    
            excluded_num = dp[s]
            # include item[i]
            included_num = dp[s-num[i]] if num[i] <= s else 0
            # number of subsets which their sum is equal to s
            dp[s] = excluded_num + included_num 
    
    return dp[sum]


def main():
  print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
  print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()
