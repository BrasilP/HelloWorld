

# String Methods



# .upper()

# the upper string method allows you to make everything in a string upper case
all_low = "there are no capitals here."
print(all_low.upper())
# THERE ARE NO CAPITALS HERE.


# .lower()
all_up = "THIS IS SHOUTING TEXT!"
print(all_up.lower())
# this is shouting text!



# .isupper  (boolean is returned)
print("Mixed Case".isupper())
# false
print("ALL CAPS!".isupper())
# true


# .islower
print("AHHHH!".islower())
# false
print("$100 is a lot to make it in an hour".islower())
# true




# ##################################Other String Methods


# .isalpha() - Only returns true if letters
print("Batman".isalpha())
# true
print("Batman123".isalpha())
# false


# .isalnum() - Only returns true if numbers and letters
print("Batman123".isalnum())
# true
print("Batman".isalnum())
# true
print("123".isalnum())
# true



# isdecimal() - Only returns true if numbers and without punctuation
print("123".isdecimal())
# true
print("3.14".isdecimal())
# false



# isspace() - Only returns true if only spaces
print(" ".isspace())
# true
print("                   ".isspace())
# true
print("not just spaces".isspace())
# false
print("not just spaces"[3].isspace())
# true




# istitle() - Only returns true if the string first letter has been capitalized
print("The Empire Strikes Back".istitle())
# true
print("Super Smash Brothers: Ultimate!".istitle())  # works with punctuation
# true



# .title() - makes the string titlecase
print("the great gatsby".title())
# The Great Gatsby