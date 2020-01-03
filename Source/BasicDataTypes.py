
# Basic Data Types


# Floating-Point Numbers

float_1 = 1.2345
print(float_1)

float_2 = -1.25
print(float_2)

float_3 = 0.0
print(float_3)

float_4 = 13.0
print(float_4)

float_5 = -0.5
print(float_5)


# Important ! On Floats (approximation errors that occur when using decimal numbers in python expressions)

# in this example, the result should be /// but the printed value was 4.029999999999999
print(1.23 + 2.80)

# The reason is because python is built on top of C. There are 2 way to go around and resolve this problem (convert
# into integers first

# First way
ex2 = (123 + 280) / 100
# 4.03
print(ex2)

# Second way
ex3 = 1.23 + 2.80
print(round(ex3, 2))





# Integers

int_1 = 7
print(int_1)

int_2 = -52
print(int_2)

int_3 = 0
print(int_3)

int_4 = 900
print(int_4)

int_5 = -749
print(int_5)



# Booleans

bool_1 = True
print(bool_1)

bool_2 = False
print(bool_2)

