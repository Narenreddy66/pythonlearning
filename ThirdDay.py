# user input

a=input("ENTER THE NAME:")
print("my name is",a)

 
# Strings Slicing

# Strings are immutable

names='naren,shydnhn'
print(names[0:8])
print(len(names))
# in this when we take negitive value it takes infront lentghofvaraible
print(names[0:-2])

nm="Harry"
print(nm[-4:-2])


# StringMethods

a="naren!!!!"
# upper method
print(a.upper())

# lower method
print(a.lower())

# rstrip :it means remove infrontspecial charcters
print(a.rstrip('!!!'))

# replace
print(a.replace('naren!!!!',"sai"))

# split :gives into list
print(a.split(" "))

# captalize
print(a.capitalize())

# center
str1="snejjwj3u3u3u3uwu3"
print(str1.center(15,','))

# count
print(a.count('n'))

# endswith(): it gives whether it is true or false
print(a.endswith('!!!!'))

# find
str2="he is a good man"
print(str2.find('a'))

# isalnum:True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False
str1 = "WelcomeToTheConsole"
print(str1.isalnum())

# isalnum:True only if the entire string only consists of A-Z, a-z,  If any other characters or punctuations are present, then it returns False
str1 = "Welcome1 22"
print(str1.isalnum())


# islower():
# The islower() method returns True if all the characters in the string are lower case, else it returns False.
# Example 1:
str1 = "hello World"
print(str1.islower())

# isprintable():
# The isprintable() method returns True if all the values within the given string are printable, if not, then return False.

# Example 1:

str1 = "We wish you a Merry Christmas"
print(str1.isprintable())

# Example 2:

str2 = "Hello, \t\t.Mike"
print(str2.isprintable())

# isspace():
# The isspace() method returns True only and only if the string contains white spaces, else returns False.

# Example 1:
str1 = "        "  # using Spacebar
print(str1.isspace())
str2 = "        "  # using Tab
print(str2.isspace())

# istitle():
# The istitle() returns True only if the first letter of each word of the string is capitalized, else it returns False.

# Example 1:

str1 = "World Health Organization"
print(str1.istitle())


# swapcase():
# The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.

# Example:

str1 = "Python is a Interpreted Language"
print(str1.swapcase())

# title():
# The title() method capitalizes each letter of the word within the string.

# Example:

str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())