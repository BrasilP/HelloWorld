

# LOOPS




# While Loops

counter = 0


while counter < 3:
    print("something")
    counter += 1





# Sum of Numbers From a Positive Integer counting down to 1 example


# pos_int is a variable which holds a user entered integer.
pos_int = int(input("Please enter a positive integer."))
# This variable stores the initial value of pos_int before it is used in the loop so
# that later it can be used to display pos_int's initial value in the output.
int_init = pos_int
# This is a variable which will be used to hold the sum of all the integers from pos_int.
summed = 0
# The while loop will run while pos_int's stored integer value is greater than 0
while pos_int > 0:
    # This is the equivalent of summed = summed + pos_int
    # In other words: new value of summed = old value of summed + new value of pos_int
    summed += pos_int
    # This will decrement pos_int so that pos_int will eventually equal 0 and the while
    # loop will stop running its code.
    pos_int -= 1

print(int_init)  # displays the initial value of pos_int
print(summed)  # displays the sum of integers from pos_int





# FOR LOOPS

word = "house"


for letter in word:
    print(letter)




# Find the number of characters in A String example

user_str = input("Please enter a string.")

count = 0  # This variable will be used to hold the number of characters in the string.
# This for loop adds 1 to count for each character in user_str.
for char in user_str:
    count += 1

print(user_str)
print(count)





# RANGE

# its a function that returns a sequence of numbers and is usually used for iterating over with a for loop. It can
# take 3 arguments start, stop and step and can be used with 1, 2 or all 3 arguments at the same time.


# using range with 1 argument
one_input = range(5)


for num in one_input:
    print(num)
# 0,1,2,3,4
# note: the name of the variable that holds the iterated items 'num' is this case should reflect the type of items
# in its name (good practice).




# using range with 2 arguments
two_inputs = range(5, 10)


for num in two_inputs:
    print(num)
# 5,6,7,8,9




# using range with 3 arguments
three_inputs_increase = range(1, 20, 3)  # 1(start), 20(stop), 3(step) * the printed items increase in this example


for num in three_inputs_increase:
    print(num)
# 1,4,7,10,13,16,19



# the printed items can also decrease in this example
three_inputs_decrease = range(20, 1, -3)  # 20(start), 1(stop), -3(step) * the printed items decrease in this example


for num in three_inputs_decrease:
    print(num)
# 20,17,14,11,8,5,2



# FIZ BUZZ example

# Write a program that prints the integers 1 through 50 using a loop.
#
# However, for numbers which are multiples of both 3 and 5 print “FizzBuzz” in the output. For numbers which are
# multiples of 3 but not 5 print “Fizz” instead of the number and for the numbers that are multiples of 5 but
# not 3 print “Buzz” instead of the number.
#
# All of the remaining numbers which are not multiples of 3 or 5 should just be printed as themselves.



for num in range(1, 51):
    # If num is divisible by both 3 and 5, "FizzBuzz" will be printed.
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    # If num is only divisible by 3, "Fizz" will be printed.
    elif num % 3 == 0:
        print("Fizz")
    # If num is only divisible by 5, "Buzz" will be printed.
    elif num % 5 == 0:
        print("Buzz")
    # num itself will be printed in all other cases.
    else:
        print(num)





# FACTORIAL example

# Create a function which takes one positive integer as its input and returns its factorial.
#
# To make sure that your function works correctly, you should call it with the inputs 3, 4, and 5 and print
# what is returned by those calls. For those inputs, you should get 6, 24, and 120, respectively.


# The argument fac_num's name is short for factorial number.
def factorial(fac_num):
    # The local variable returned will be used in the for loop used to calculate fac_num's
    # factorial. To do this, it will be multiplied by decrementing values of
    # fac_num. Since it will be multiplied, it was given the initial value of 1.
    returned = 1
    # By the end of this for loop, returned will have been reassigned fac_num's factorial.
    for item in range(fac_num, 1, -1):
        returned *= item

    # returns returned, which now holds the value of fac_num's factorial
    return returned


print(factorial(3))  # 6
print(factorial(4))  # 24
print(factorial(5))  # 120

