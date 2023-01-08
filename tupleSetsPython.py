# TUPLE
flowers_tuple = ("roses", "sunfloweres", "daisies")

print(flowers_tuple) # PRINTS ("roses", "sunfloweres", "daisies")
print(flowers_tuple[1]) # PRINTS (roses)

"""
Tuples are similar to lists.
They are used to store multiple items in a 
single variable.
As a collection of data, tuples are ordered and 
immutable (unchangable).
"""
# SETS

flowers_set = {"roses", "sunflowers", "daisies"}

print(flowers_set)
"""
Sets are another data type that allow 
us to store multiple elements together.
Unlike tuples, sets are not ordered or indexed.
Elements in a set must be immutable, but sets 
themselves are mutable (we can add and 
remove elements).
Sets do not allow duplicates. If a duplicate 
element is added, it will be ignored.
"""

"""
Tuples
Immutable(unchangeable
Accepts any data type
Ordered and indexed
Allows duplicates
Written with parentheses()

Sets 
Mutable(changeable(
Accepts any data type
Unorded
Doesnt allow duplicates
Written with curly brackets {}
"""

# CONDITIONAL STATEMENTS

weather = "rain"

if weather == "rain":
    print("Bring an umbrella")
    if weather == "sunny":
        print("Have a great day!")
    else: 
            print("Look out the window!")


# CONDTITIONALS

2 < 3
10 > 5
10 == 10
city = "Dallas"

if city != "Houston":
    print('Not the best city on Earth')