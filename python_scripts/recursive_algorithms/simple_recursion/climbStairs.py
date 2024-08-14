"""
QUESTION: leetcode question 70: climbing stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45

"""

#recursive case
#           step 3
#     step 1              step  2
#     step 0         step 1        step 0   
#                    step 0
        

def climbStairs(n):
    #base case
    if n == 0:
        return 1
    elif n == 1:
        return 1
    #recursive case
    else:
        return climbStairs(n-1) + climbStairs(n-2)


print(climbStairs(4))


"""
THIS WOULD BE AN IN EFFICIENT FOR LARGER VALUES OF n such as 48
One optimised solution would be the use of MEMOIZATION.
- memoization using a dictionary, or
- memoization using from functools import lru_cache
"""
