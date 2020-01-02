
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


