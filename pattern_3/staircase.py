def count_ways(n):
    if n < 2:
        return 1
    if n == 2:
        return 2

    # base case
    # for n == 0, we don't need to take any step, so there is only one way
    s1 = 1
    s2 = 1
    s3 = 2

    for i in range(3, n+1):
        s = s1 + s2 + s3
        s1 = s2 
        s2 = s3
        s3 = s
    return s

def main():
    print(count_ways(3))
    print(count_ways(4))
    print(count_ways(5))


main()
