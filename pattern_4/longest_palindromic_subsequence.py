def find_LPS_length(st):
    n = len(st)
    dp = [[0 for j in range(n)] for i in range(n)]

    # every sequence with one element is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1

    # startIndex starts from the last string and move up to the first
    for startIndex in range(n - 1, -1, -1):
        for endIndex in range(startIndex + 1, n):
            # elements at the beginning and the end are the same
            if st[startIndex] == st[endIndex]:
                dp[startIndex][endIndex] = 2 + dp[startIndex + 1][endIndex - 1]
            # skip one element either from the beginning or the end
            else:
                dp[startIndex][endIndex] = max(dp[startIndex + 1][endIndex], dp[startIndex][endIndex - 1])
 
    return dp[0][n-1]


def main():
  print(find_LPS_length("abdbca"))
  print(find_LPS_length("cddpd"))
  print(find_LPS_length("pqr"))


main()