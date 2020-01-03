

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





# .startswith
print("this is a string".startswith("this"))
# true
print("this is a string".startswith("t"))
# true
print("this is a string".startswith("T"))
# false



# .endswith
print("to the infinity and beyond!".endswith("beyond!"))
# true
print("to the infinity and beyond!".endswith("beyond"))
# false



# .join
print("".join(["one", "two", "three"]))
# onetwothree
print(" ".join(["one", "two", "three"]))
# one two three
print(",".join(["one", "two", "three"]))
# one,two,three
print("...".join(["one", "two", "three"]))
# one...two...three



# .split
print("Eggs, Milk, Waffles, Bacon".split())
# ['Eggs,', 'Milk,', 'Waffles,', 'Bacon']
print("Eggs, Milk, Waffles, Bacon".split(","))
# ['Eggs', ' Milk', ' Waffles', ' Bacon']
print("Eggs, Milk, Waffles, Bacon".split(", "))
# ['Eggs', 'Milk', 'Waffles', 'Bacon']





# .rjust
print("hello world".rjust(15))
#     hello world (4 spaces on the left side + 11 hello world chars makes 15)


# .ljust
print("hello world".ljust(15) + "four spaces added to the right of hello world.")
# hello world    four spaces added to the right of hello world.

print("hello world".rjust(15, "-"))
# ----hello world
print("hello world".ljust(15, "*"))
# hello world****




# .center
print("hello world".center(15))
#   hello world  (a centered hello world)
print("hello world".center(15, ":"))
# ::hello world::





# .strip
print("111 I had an exciting trip!!!!1111".strip("1"))  # removes 1 from both sides of the string
# I had an exciting trip!!!!
print("blueblueyellowblue".strip("eulb"))
# yellow


# .rstrip
print("111 I had an exciting trip!!!!1111".rstrip("1"))  # removes 1 from the right side of the string
# 111 I had an exciting trip!!!!
print("juice, bread, cheese, beef, bread".rstrip(", bread"))  # removes the second bread of the string
# juice, bread, cheese, beef
print("juice, bread, cheese, beef, bread".rstrip(", ed arb"))  # same result as above. Reads from left to right
# juice, bread, cheese, beef


# .lstrip
print("111 I had an exciting trip!!!!1111".lstrip("1"))  # removes 1 from the left side of the string
#  I had an exciting trip!!!!1111





# .replace
print("Good morning.".replace("morning", "afternoon"))
# Good afternoon.




# len
print(len("tree"))
# 4
print("This" + " " + "is a " + "string.")
print(len("This" + " " + "is a " + "string."))
# 17
print("antidisestablishmentarianism"[7:20])
print(len("antidisestablishmentarianism"[7:20]))
# 13





# String Reverser example
user_string = input("Please enter a string.")
reversed = ""


for item in range(len(user_string) - 1, -1, -1):
    reversed += user_string[item]


print(reversed)





# Word Counter example
str_1 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
shrimp burger, shrimp sandwich. That- that's about it."

spaces_and_letters = ""

# this for loop reduces the string to letters, numbers, and spaces
for char in str_1:
    if char.isalnum() or char.isspace():
        spaces_and_letters += char


words = spaces_and_letters.split()
number_of_words = len(words)


print(words)
print(number_of_words)







# String Concatenation


name = input("What is the job applicant's name?")
degree = input("What did they major in at college?")
job = input("What is their current occupation?")
experience = input("How many years have they been working in their field?")

print(name + " majored in " + degree + ", works as a " + job + ", and has " + experience + " years of experience.")
# Adam majored in Economics, works as a Manager, and has 7 years of experience.


# the following is a recommended solution for the above string concatenation as it can get messy.
name = input("What is the job applicant's name?")
degree = input("What did they major in at college?")
job = input("What is their current occupation?")
experience = input("How many years have they been working in their field?")

print("{} majored in {}, works as a {}, and has {} years of experience.".format(name, degree, job, experience))
# Adam majored in Economics, works as a Manager, and has 7 years of experience.








