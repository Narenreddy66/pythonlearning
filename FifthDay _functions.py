# Python Functions

# 1. built-in functions:
# These functions are defined and pre-coded in Python. Some examples of built-in functions are as follows:

# min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.

# 2. user-defined functions:
# We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.

# Syntax:

# def function_name(parameters):
#     Code and Statements

# cal a function

def main_data(name, refe):

    print("This is My Name" + ":" + name + "my class is " + ":" + str(refe))

main_data("narendhar",12)


# Function Arguments
# Default arguments:by default arguements we can give
def name(fname,mani="manikanta",money="not tere") :
    print("hello " +" "+fname +"." + mani + "," + "dont" +" " + money)
name("narenhar")  

# Keyword arguments: we give this key:value in arguments
def care(drink,money):
    print("Mani" + drink ,money)
care(drink="too much", money=4000)

# Required arguments: we need to pass all arguents
def required(value,i):
    print("hello"+ "," + str(value),i)
required(238,i=8339)

# varaible length arguments:Some times we need to pass more value to single arguments 
# 1.arbitary: while declaring tje function we use *
def name(*lmit):
    print("hello" + "," + lmit[0],lmit[1])
name("dwdkk","oieioeio")    
# 2.keyword: we pass** here
def items(**name):
    print("hiii" + "," + name[ "mname"]+name["lname"])
items(mname='ede',lname="eijerji")    

# return statement:return the values to the mainfubction
def stmt(mcal,ncal):
    return "hello " +","+"mu banem" +ncal  + mcal 
print(stmt("djdjd","dwjwdj"))

# Python Recursion
# function call iself

def factorial(num):
    if ( num==1 or num==2):
        return 10
    else:
        return (num * factorial(num -1))
    
num=1
print(num)
print(factorial(num))    
