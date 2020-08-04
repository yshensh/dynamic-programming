import math

def count_min_jumps(jumps):
    n = len(jumps)
    # initialize with infinity, except the first index which should be zero as we start from there
    dp = [math.inf for i in range(n)]
    dp[0] = 0

    for start in range(n - 1):
        end = start + 1
        while end <= start + jumps[start] and end < n:
            # every index within the range of current index can be reached in one jump
            dp[end] = min(dp[end], dp[start] + 1)
            end += 1
    return dp[n - 1]


def main():

  print(count_min_jumps([2, 1, 1, 1, 4]))
  print(count_min_jumps([1, 1, 3, 6, 9, 3, 0, 1, 3]))


main()