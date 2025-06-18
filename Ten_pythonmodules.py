# Python Modules

#exception handling

# print(f"my enter number is {a}")
try:
 a=int(input("Enter a number:"))

 for i in range(1,11):
     print(f"addition of thr nuber:{a}={a*i}")
except ValueError:
   print("this is not an interger")     
except Exception as e:
    print(f"This is not a number {e}")   
else:
   print("iam ok") 

# try:
#     a = int(input("Enter a number: "))
#     print(f"My entered number is {a}")
    
#     for i in range(1, 11):
#         print(f"{a} x {i} = {a * i}")

# except ValueError:
#     print("This is not a valid number. Please enter an integer.")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
# else:
#     print("Multiplication table printed successfully!")

#     Here are some popular python built-in modules:

# csv, datetime, json, math, random, sqlite3, statistics, tkinter, turtle, etc.


import math

print("Sin(0)=" ,math.sin(0))
print("Sin(45)=",math.sin(math.pi/4))

# Creating and using module:
# import module
# num1= int(input("Enter the number:"))
# num2=int(input("ENter the number2:"))
# print("Addition =" ,module.add(num1,num2))
# print("Sub =" ,module.sub(num1,num2))

# print("mutliply =" ,module.multiply(num1,num2))

# print("div =" ,module.div(num1,num2))


# B. Using an alias:

import module as m
try:
 num1= int(input("Enter the number:"))
 num2=int(input("ENter the number2:"))
 print("Addition =" ,m.add(num1,num2))
 print("Sub =" ,m.sub(num1,num2))

 print("mutliply =" ,m.multiply(num1,num2))
 
 print("div =" ,m.div(num1,num2))
except ValueError:
 print("plese ernter the integer only")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
except Exception as e:
  print(f"plese enetr the {e}")

# C. import from module:
# You can also import specific parts that you need from a module instead of importing the entire module.


from module import add, sub
 
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
 
print("Addition", add(num1, num2))
print("Subtraction", sub(num1, num2))
print("Multiplication", multiply(num1, num2))
print("Division", div(num1, num2))


# Use an asterisk (*) while importing.

# Example:

from module import *
 
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
 
print("Addition", add(num1, num2))
print("Subtraction", sub(num1, num2))
print("Multiplication", multiply(num1, num2))
print("Division", div(num1, num2))


import module
list1=dir(module)
print(module)