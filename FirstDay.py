print('helloworld')

# This is Day 1

# Variables
a = 1
b = 'anrend'
c = False

# Global variable reassigned
a = 2

def naren():
    print("this is " + str(a))  # Accessing global variable 'a'

naren()

# Local variables inside function (not affecting global scope)
def local():
    a = 2
    b = "narendar"
    print("this is " + str(a) + b)  # Added space between a and b

local()


NameOfCity = "Mumbai"       # Pascal case
nameOfCity = "Berlin"       # Camel case
name_of_city = "Moscow"     # snake case