# Fibonacci Sequence
# 1, 1, 2, 3, 5, 8, 13
# F(0) = 0; F(1) = 1; F(2) = 1;
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.

# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

# Constraints:
# 0 <= n <= 30
def fib(n: int) -> int:

    #base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    #recursive case
    else:
        return fib(n-1) + fib(n-2)


print(fib(7))
