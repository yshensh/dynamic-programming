def calculateFibonacci(n):
    if n < 2:
        return n
    
    # Fibonacci numbers are a series of numbers in which each number is the sum of the two preceding numbers
    n1 = 0
    n2 = 1
    for i in range (2, n+1):
        fib = n1 + n2
        n1 = n2
        n2 = fib
    return fib

def main():
    print("5th Fibonacci is ---> " + str(calculateFibonacci(5)))
    print("6th Fibonacci is ---> " + str(calculateFibonacci(6)))
    print("7th Fibonacci is ---> " + str(calculateFibonacci(7)))


main()