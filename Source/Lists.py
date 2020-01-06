

# Lists


print(list("blah"))
# ['b', 'l', 'a', 'h']


# IN

checked_list = [1, 2, 3, 4]
print(1 in checked_list)
# true

checked_list = [1, 2, 3, 4]
print(8 in checked_list)
# false




# NOT IN

checked_list = [1, 2, 3, 4]
not_in_example = 8 not in checked_list
print(not_in_example)
# true

checked_list = [1, 2, 3, 4]
not_in_example = 2 not in checked_list
print(not_in_example)
# false



# Index and list slicing

indexes_example = ["carpet", "hardwood", "linoleum"]
print(indexes_example[1])
# hardwood

indexes_example_two = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(indexes_example_two[2][0])
# 7 (being '2' the index of the list and '0' the index of the specified list



# negative

negative = [1, 2, 3, 4, 5]
print(negative[-1])
# 5



# List slicing

sliced = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sliced[:4])
print(sliced[3:8])
print(sliced[6:])
# [1, 2, 3, 4]
# [4, 5, 6, 7, 8]
# [7, 8, 9]



# index list reassignment

example = [2, 4, 6, 8, 0]
print(example)
example[3] = 10
print(example)
# [2, 4, 6, 8, 0]
# [2, 4, 6, 10, 0]

example_two = [2, 4, 6, 8, 0]
print(example_two)
example_two[1:4] = [3, 2, 1]
print(example_two)
# [2, 4, 6, 8, 0]
# [2, 3, 2, 1, 0]

example_three = [2, 4, 6, 8, 0]
print(example_three)
example_three[4:7] = [7, 6, 5]
print(example_three)
# [2, 4, 6, 8, 0]
# [2, 4, 6, 8, 7, 6, 5]




# DEL Statements

planets = ["pluto", "mars", "earth", "venus"]
del planets[0]
print(planets)
# ['mars', 'earth', 'venus']



# .remove

planets_two = ["pluto", "mars", "earth", "venus"]
planets_two.remove("pluto")
print(planets_two)
# ['mars', 'earth', 'venus']


# .pop
# removes and returns the last item from a list (if no argument passed) to be used in another part of the code

bands = ["Queen", "Led Zeppelin", "The Beatles", "MUSE", "Radiohead"]
end = bands.pop()
print(bands)
print(end)
# ['Queen', 'Led Zeppelin', 'The Beatles', 'MUSE']
# Radiohead


# passing the index as an argument to remove and return a specific string
bands_two = ["Queen", "Led Zeppelin", "The Beatles", "MUSE", "Radiohead"]
end = bands_two.pop(3)
print(bands_two)
print(end)
# MUSE







# .append
# (to add an item to the end of a list)

pets = ["cat", "dog", "parrot"]
print(pets)
pets.append("fish")
print(pets)
# ['cat', 'dog', 'parrot']
# ['cat', 'dog', 'parrot', 'fish']



# .insert
# (to add an item to a specified index of a list

pets_twos = ["cat", "dog", "parrot"]
pets_two.insert(1, "turtle")
print(pets_two)
# ['cat', 'turtle', 'dog', 'parrot']



# .sort
# (to order from its lowest value to the highest value

num_list = [2.718, 4, -19, 10000, 0]
print(num_list)
num_list.sort()
print(num_list)
# [2.718, 4, -19, 10000, 0]
# [-19, 0, 2.718, 4, 10000]

str_list = ["Ringo", "John", "George", "Paul"]  # .sort uses ASCIIbetical order meaning that if there were strings
print(str_list)                                 # starting with lowercase, python would not order them correctly.
str_list.sort()                                 # another approach described bellow is suggested for this.
print(str_list)
# ['Ringo', 'John', 'George', 'Paul']
# ['George', 'John', 'Paul', 'Ringo']

ASCIIbetical = ["Andy", "kiwi", "apple", "Karen", "Brian", "banana"]
ASCIIbetical.sort()
print(ASCIIbetical)
ASCIIbetical.sort(key=str.lower)
print(ASCIIbetical)
# ['Andy', 'Brian', 'Karen', 'apple', 'banana', 'kiwi']
# ['Andy', 'apple', 'banana', 'Brian', 'Karen', 'kiwi']




# sort reverse
# to reverse the sort order

num_list_two = [2.718, 4, -19, 10000, 0]
str_list_two = ["Ringo", "John", "George", "Paul"]
print(num_list_two)
print(str_list_two)
num_list_two.sort(reverse=True)
str_list_two.sort(reverse=True)
print(num_list_two)
print(str_list_two)
# [2.718, 4, -19, 10000, 0]
# ['Ringo', 'John', 'George', 'Paul']
# [10000, 4, 2.718, 0, -19]
# ['Ringo', 'Paul', 'John', 'George']




# .index
# to find out the index of a specific string

metals = ["copper", "gold", "silver", "iron"]
print(metals.index("silver"))
# 2











