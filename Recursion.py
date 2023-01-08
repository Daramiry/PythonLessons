# What is recursion

'''Recursion iswhen a function calls
itself over and over until it reaches a 
specified stopping condition


The process of describing an action in terms
of itself
'''

# Two Parts of Recursive Functions

'''Base case: When a condition has been reached, calls to the same function stop.

Recursive case: when the functin calls itself again and again until the desired
bse case is met
'''

# Recursion Example - Factorial

def find_fact(num):
    # // base case
    if num == 1:
        return 1

    # // recursive case
    else:
        return (num * find_fact(num-1))

n = 4
print(find_fact(n))

# Examples
'''
•4! = 4*3*2*1 = 24
•7! = 7*6*5*4*3*2*1 
•= 7*6*5*24 = 5040
'''

# Factorial Example
find_fact(5)
"""5! = 5 * 4! # Recursive
        4! = 4 * 3! # Recursive
            3! = 3 * 2! # Recursive
                2! = 2 * 1 # Base
"""

# Recursive and Iterative Solution comparison

