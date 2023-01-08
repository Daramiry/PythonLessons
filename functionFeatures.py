#function discription

""" def """ # <--- key word 
""" function name """ # could be any name to a function
""" () """ # <------parameters enclosed by paratheses
""" : """ # <------ closing colon


# python functions: Multiple Returns
"""
Python functions are able to return 
multiple values.
Multiple return values should be listed 
after the return keyword and 
separated by a comma.
When multiple values are returned
"""

def two_returns (param1, param2):
    value1 = param1 + param2
    value2 = param2 - param1
    return value1, value2

way1 = two_returns(1,2)
#way1 is now (3,-1)

way2, way3 = two_returns(1,2)
#way2 is 3
# way3 is -1

"""
    When a function returns multiple 
values, there are two ways to handle it: 
as a single tuple object, or as multiple 
objects.
By using the same number of variables 
as returned values, we can "catch" 
each value independently, instead of 
iterating to grab each value.
"""

# Nested Functions
def inner_funcs (int_param):

    # inner function definition
    def minus_five (inner_param) :
        return inner_param - 5

    # inner function call 
    new_val = minus_five(int_param)

    # returned value based on inner function
    return new_val

"""
Just as in JS, Python functions may 
contain one or more internal (or 
nested) functions.
"""

# Default Arguements

#declare function with default arguement
def default_add(a, b=20):
    return a + b

# Will output 8
sum1 = default_add(3, 5)

# will output  8 
sum2 = default_add(4)

"""
As in JS, Python functions may accept 
default arguments when declaring a 
function by using the assignment 
operator (=).
Important! Once a default argument 
has been declared, all subsequent 
arguments must also have default 
values in Python.
"""

# Arbitray Arguments (*args)

def print_all(*args):
    print(args)

print_all('str1', 1, 'str2', true)

# Output:

('str1', 1, 'str2', true)

"""
Python functions may accept an 
arbitrary number of arguments through 
use of the unpacking operator (*).
"""

# Arbitrary Arguemnts (*args)

def print_list (*names):
    for i in names:
        print (i)

print_list('anne', 'trevor', 'eli', 'marcus')

# output
'''
anne
trevor
eli
marcus
'''
"""
The unpacking operator (*) creates an 
iterable tuple.
Any parameter name may be used 
after the unpacking operator (*). *args 
is the standard when passing in a 
function argument.
The unpacking operator can be used in other 
places besides passing in function arguments.
"""