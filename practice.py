# USING PRINT

x = 5
print(x)
#prints 5

my_string = "format"
print(f"In Python, Iam called {my_string} string.")
#prints: In Python, I am called a format string.

print(x, my_string)
#print 5 format

print(x + my_string)
#prints: 5format

# FUNCTIONS 

def intro(name): 
    print("Hey" + name)

intro("Sal") #output: Hey Sal

# WRITTING COMMENTS
def intro(name):
    """" <-------------------------------------- use for multiple comment lines
    This function prints a string with a greeting.
    It does not have a return value
    """

    #Print a greeting <------ use for one line comments
    print("Hey" + name)

    # LIST

    months_list = ["Sept", "Oct", "Nov"]

    print(months_list) #["Sept", "Oct", "Nov"]

    months_list.append("Dec")
    #List is now :["Sept", "Oct", "Nov", "Dec"]

    months_list.remove("Oct")
    #List is now :["Sept", "Nov", "Dec"]

    #STRINGS    

    my_string = "Hello World"
    print(my_string)
    
    #DICTIONARY

    my_dict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1994
    }

print(my_dict)