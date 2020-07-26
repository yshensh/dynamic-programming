import math

def count_ribbon_pieces(ribbonLengths, total):
    n = len(ribbonLengths)

    # initialize dp[i][t] structure
    dp = [[-math.inf for t in range(total+1)] for i in range(n)]

    # initialize dp[i][0]
    for i in range(n):
        dp[i][0] = 0

    # derive dp[i][t], which represents the max number of pieces (given ribbonLengths[i]) need to form length 't'
    for i in range(n):
        print("----------- i: {} ------------".format(i))
        for t in range(1, total+1):
            exclude_ribbon = dp[i-1][t] if i - 1 >= 0 else -math.inf
            include_ribbon = dp[i][t-ribbonLengths[i]] + 1 if t-ribbonLengths[i] >= 0 else -math.inf
            dp[i][t] = max(exclude_ribbon, include_ribbon)
        print(dp)    
    return -1 if dp[n-1][total] == -math.inf else dp[n-1][total]
    

def main():
  print(count_ribbon_pieces([2, 3, 5], 5))
  print(count_ribbon_pieces([2, 3], 7))
  print(count_ribbon_pieces([3, 5, 7], 13))
  print(count_ribbon_pieces([3, 5], 7))


main()