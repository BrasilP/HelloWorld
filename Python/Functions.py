

# Functions

# Note
# After defining a function, you should have 2 blank lines after it before creating more code. Its a practice that is in
# accordance to the python style guide pep8


# ex_1
def function_name():
    print(2 + 2)


function_name()
# 4





# ex_2
def function_name_two(parameter):
    print(parameter + 2)


# passing an argument of value = 8
function_name_two(8)
# 10





# ex_3
# when you define a function, you can create as many parameters as you want.
first_str = "The number "


def function_name_three(p1, p2, p3):
    print(p1 + str(p2) + p3)


function_name_three(first_str, 5, " is an integer.")
# The number 5 is an integer.




# Function with default parameters
# ex_4
def default_example(num1=7, num2=8):
    print(num1 * num2)


default_example()
# 56



# passing arguments to a function with default values
# ex_5
def default_example_two(num1=7, num2=8):
    print(num1 * num2)


default_example_two(4, 6)
# 24




# function that returns a value instead of printing it
# ex_6
def default_example_three(num1=7, num2=8):
    return num1 * num2


print(default_example_three() + 44)
# 100





# Celsius to Fahrenheit function with integers
celsius = int(input("Please enter an integer value for degrees celsius. "))


def fahrenheit(cel):
    # To avoid the approximation error that would occur if the float 1.8 was used in the calculation, 1.8 * 10 is used
    # instead, resulting in the integer 18.  To balance this out, 32 is also multiplied by 10 to get 320.  After the
    # calculations in the parentheses are finished, the result is divided by 10, which gives the correct Fahrenheit
    # temperature.
    return (18 * cel + 320) / 10


print("The Fahrenheit equivalent of " + str(celsius) + " degrees Celsius is " + str(fahrenheit(celsius)) + ".")







# Celsius to Fahrenheit function with round
celsius = int(input("Please enter an integer value for degrees celsius. "))


def fahrenheit(cel):
    # The second argument of round() is 1 since we only want the Fahrenheit temperature to be displayed with 1 number
    # after the decimal point
    return round((1.8 * cel + 32), 1)


print("The Fahrenheit equivalent of " + str(celsius) + " degrees Celsius is " + str(fahrenheit(celsius)) + ".")





# ###########################################Importing Modules


# Generic imports
import random


print(random.randint(1, 10))
# prints a number >= 1 & <= 10 from the called randint function



# Function imports
from random import randint


print(randint(10, 20))
# prints a number >= 10 & <= 20 from the called randint function




# Universal imports
from random import *


print(random())
# the random function returns a float value which is >= 0.0 & <= 1.0 when it is called






# Miles Per Gallon (using the random function)
from random import randint
# generates random integer between and inclusive of 10 and 25 to represent gas in the car's fuel tank
fuel = randint(10, 25)
# generates random integer between and inclusive of 200 and 400 to represent miles the car can go without refueling
miles = randint(200, 400)
# calculates and displays the MPG of the car assuming car manufacturers overestimates in their claims
print("The car can travel " + str(miles // fuel) + " miles per gallon.")
# displays the number of gallons of fuel that the car's fuel tank can hold
print("The car's fuel tank can hold " + str(fuel) + " gallons.")
# displays the number of miles that the car can travel on a full tank
print("The car can travel " + str(miles) + " miles on a full tank.")






# ###################################### Variable Scope

# variables created within function have a local scope and variables created outside of functions have a global scope.

example = "hello world"     # global


def loc_ex():
    example = "this is a string"        # local
    return example


print(example)
print(loc_ex())
