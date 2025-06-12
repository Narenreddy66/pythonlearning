# Numeric data: int, float, complex
# int: 3, -8, 0
# float: 7.349, -9.0, 0.0000001
# complex: 6 + 2i



# Text data: str
# str: "Hello World!!!", "Python Programming"

# Boolean data:
# Boolean data consists of values True or False.

# Sequenced data: list, tuple, range

# list: A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. Lists are mutable and can be modified after creation.

# Example:

list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)


# tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses. Tuples are immutable and cannot be modified after creation.

# Example:

tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)

# range: Returns a sequence of numbers as specified by the user. If not specified by the user, it starts from 0 by default and increments by 1.

# Example:

sequence1 = range(4,20,2)
for i in sequence1:
    print(i)

#     Mapped data: dict
# dict: A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.

# Example:

dict1 = {"name": "Sakshi", "age": 20, "canVote": True}
print(dict1)

# Set data:
# Set is an unordered collection of elements in which no element is repeated. The elements of sets are separated by a comma and contained within curly braces.

# Example:

set1 = {4, -5, 8, 3, 2.9}
print(set1)


# None:
# None is used to define a null value. When we assign a None value to a variable, we are essentially resetting it to its original empty state, which is not the same as zero, an empty string, or a False value.

# Example:

state = None
print(type(state))


# Data Conversion
# The process of converting numeric data from one type to another is called type conversion.
# To convert from integer to float, we use the float() function.
# To convert from float to complex, we use the float() function.



a=-232
b=float(a)
c=complex(a)
print("convert integer to float" + str(b))
print("convert integer to complez" + str(c))




# Type Casting
# Similar to type conversion, type casting is done when we want to specify a type on a variable.

# Example:

str1 = "7"          
str2 = "3.142"
str3 = "13"
num1 = 29
num2 = 6.67
 
print(int(str1))
print(float(str2))
print(float(str3))
print(str(num1))
print(str(num2))