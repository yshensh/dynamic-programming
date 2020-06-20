# Let p, n be the sums of numbers will be assigned with positive and negative symbols
# Let sum = p + n
# Problem conversion
# 1) p - n = s
# 2) p + n = sum
# we get n = (sum - s) / 2
#        p = (sum + s) / 2
# There for the problem is equivalent to finding integers that sum up to p or finding integers sum up to n


def find_target_subsets(num, s):
    # sum of num list
    sums = sum(num)

    # can't find any combinations that sum to s
    if (sums + s) % 2 == 1:
        return 0

    # define p
    psum = int((sums + s) / 2)

    # length of num list
    length = len(num)

    # step 0: initialize dp[i][p] which represents all possible sums with every subset
    dp = [[0 for s in range(psum+1)] for i in range(length)]
    
    # for each item in index 'i' and sum 'p'
    # 1) exclude the number at index 'i'
    #    dp[i-1][p] => count all the subsets without the given number up to the given sum
    # 2) include the number at index 'i' if its value is not more than the 'sum'. 
    #    dp[i-1][p-num[i]] => count all the subsets to get the remaining sum (s-num[i])
    
    # step 1: initialization
    # '0' sum can always be found through an empty set
    for i in range(length):
        dp[i][0] = 1

    # populate row where item index = 0
    # with only one number, we can form a subset only when the required sum is equal to the number
    for s in range(1, psum+1):
        dp[0][s] = 1 if num[0] == s else 0            

    # step 2: populate dp[i][s]
    for i in range(1, length):
        for s in range(1, psum+1):
            # exclude item[i]    
            excluded_num = dp[i-1][s]
            # include item[i]
            included_num = dp[i-1][s-num[i]] if num[i] <= s else 0
            # number of subsets which their sum is equal to s
            dp[i][s] = excluded_num + included_num 
    
    return dp[length-1][psum]


def main():
    print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
    print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))


main()
