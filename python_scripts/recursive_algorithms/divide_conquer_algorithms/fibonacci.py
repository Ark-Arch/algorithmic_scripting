# leetcode 509 - fibonacci number
# a non-optimized solution
# memoization is a step to optimising this solution.

def fib(n):
    # base case
    if n<=2:
        return 0 if n == 0 else 1
    else:
        return fib(n-1) + fib(n-2)


print(fib(10))