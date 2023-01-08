# syntax
result = lambda parameter: expression

# Example

area = lambda length, width: length * width
area(5, 5) #25

def area (legnth, width):
    return legnth * width

area (5, 5) #25

'''
•lambda - the keyword to start a lambda 
function
•parameters - a list of parameters 
•: - a colon to separate the parameters 
from the expression 
•expression - the expression to resolve
•Note that any lambda function can 
also be written as a standard function
'''

# CASE EXAMPLE

map (lambda state: state.capitlize(), ['washington', 'alaska', 'hawaii'])
#['Washington', 'Alaska', Hawaii']


# list comprehensions

'''
An elegant way to generate a list.
This is done by defining the list and its 
contents at the same time in one line.
'''

# syntax

list = [expression for element in iterable]

#example

squares = [num*num for num in range(5)]
# [0, 1, 4, 9, 16]



# set comprehensions

'''
•set - the variable to save the set to
•{} - encasing an expression and loop, 
denotes the start of a set comprehension
•expression - what to do to each 
element before putting it in the set
•for...in - loop through the iterable to 
make the new set
•if... - optional expression to filter the 
elements
'''

set = {expression for element in iterable if ...} 

#example
divisible = {num for num in range (10) if num % 2 == 0}


# dictionary comprehensions

'''
•dict - the variable to save the dictionary 
to
•{} - encasing a key, expression, and 
loop; denotes the start of a dict 
comprehension
•key: expression - what to name the 
key and do to the element before saving it 
in the dict
•for...in - loop through the iterable to 
make the new dict
'''

# syntax 
dict = {key: expression for element in iterable}

# example 
doubled = {num: num * 2 for num in range(4)}
# expected output ---> {0: 0, 1: 2, 2: 4, 3: 6}