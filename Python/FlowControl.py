
# Comparison & Boolean operators


# comparison operators
# >
# <
# >=
# <=
# !=
# ==



# Note 1
# strings, are case sensitive so the following code execution will evaluate to false

print("Hello" == "hello")
# false



# Note 2
# floats and integers can be equivalent
print(4.0 >= 4)
# true
print(4.0 <= 4)
# true
print(4.0 == 4)
# true


# Note 3
# make sure to always use == when comparing values since a single = is used to assign values to variables






# Boolean operators

# and

print(4 > 1 and "word" == "word")
# true and true == true
print(8.76 == 8.7600 and 2 != 2)
# true and false == false
print("earth" == "Earth" and 6 <= 3)
# false and false == false
print(10 == 5 and 10 != 5)
# false and true == false




# or

print(4 > 1 or "word" == "word")
# true and true == true
print(8.76 == 8.7600 or 2 != 2)
# true and false == true
print("earth" == "Earth" or 6 <= 3)
# false and false == false
print(10 == 5 or 10 != 5)
# false and true == true




# not

print(not 6482 > 0)
# not true == false
print(not "Python" != "Python")
# not false == true





# ############ IF STATEMENT

veg = input("Type the name of a vegetable")


if veg == "corn":
    print("The entered vegetable is corn.")



# ################## ELSE STATEMENT

veg = input("Type the name of a vegetable")


if veg == "corn":
    print("The entered vegetable is corn.")
else:
    print("The entered vegetable is not corn")



# ################## NESTED IF ELSE STATEMENTS

gpa = float(input("What was the applicant's grade point average?"))
inst_app = input("Is the student going to be educated at an approved institution?")


if gpa >= 3.7:
    if inst_app == "yes":
        print("The applicant qualifies for a low APR student loan.")
    else:
        print("The applicant does not qualify. Have not been accepted into an approved institution")
else:
    print("The applicant did not have high enough grades to qualify")




# a Grade Determiner example

score = int(input("Please enter the student's score. "))


if score >= 90:
    print("This student's score of " + str(score) + " is an A.")
else:
    if score >= 80:
        print("This student's score of " + str(score) + " is a B.")
    else:
        if score >= 70:
            print("This student's score of " + str(score) + " is a C.")
        else:
            if score >= 60:
                print("This student's score of " + str(score) + " is a D.")
            else:
                print("This student's score of " + str(score) + " is a F.")







# ############################elif OR ELSE IF STATEMENTS

user_num = int(input("Please enter an integer"))

if user_num < 0:
    print("The number you entered is less than 0.")
elif user_num == 0:
    print("The number you entered is 0.")
elif 0 < user_num <= 100:
    print("The number you entered can be 1, 100, or anything in between.")
else:
    print("The number you entered is greater than 100.")




# Roman Numeral Equivalent example

from random import randint

one_to_ten = randint(1, 10)

if one_to_ten == 1:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is I.")
elif one_to_ten == 2:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is II.")
elif one_to_ten == 3:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is III.")
elif one_to_ten == 4:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is IV.")
elif one_to_ten == 5:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is V.")
elif one_to_ten == 6:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is VI.")
elif one_to_ten == 7:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is VII.")
elif one_to_ten == 8:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is VIII.")
elif one_to_ten == 9:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is IX.")
else:
    print("The roman numeral equivalent of " + str(one_to_ten) + " is X.")





# Truthy and Falsey values

strings_example = input("Enter any string other than an empty one.")


if strings_example != "":
    print("Thank you for entering something.")
else:
    print("You did not entered a string")


# You could also use the bool function to return true or false values
print(bool(""))
# false
print(bool("01234"))
# true
print(bool("This is a string"))
# true








