# Some other cool things we can do with list

# membership checks with "in" keyword: to check if an item is IN a list, returns a Boolean value

guest_list = ["Adam", "Bob", "Charlie", "James", "Dylan", "Ethan"]

print("Albert" in guest_list) # should return False 
print("Dylan" in guest_list) # should return True 

name = input("What's your name? ") #Travis

guest_list.append(name)

# using "if" statment wiht the "in" keyword to check if a name is already in the list
if name in guest_list:
    print("Welcome to the party: ", name + "!!!")
else:
    print("Scraaaam fool!!!")

print("="*50)

# using "not in" keyword to check if a name is NOT in the list
guest_list = ["Adam", "Bob", "Charlie", "James", "Dylan", "Ethan"]

print("Albert" in guest_list) # should return False 
print("Dylan" in guest_list) # should return True 

name = input("What's your name? ") #Travis

# guest_list.append(name) - removing the append which added the name automatically we can look and see it is NOT in the list

# using "if" statment wiht the "in" keyword to check if a name is already in the list
if name in guest_list:
    print("Welcome to the party: ", name + "!!!")
elif name not in guest_list:
    print("Scraaaam fool!!!")

print("="*50)

# meerge list together with a "+" operator
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = list1 + list2
print(list3)

# Copying a list with the ".copy()" method
# changes made to a true copy do not affect the original list

fruit = ["apples", "bananas", "oranges"]
copy_fruit = fruit.copy()
print("copy_fruit")
copy_fruit.pop() #pops out the last value so (orenges will not show)
print("copy_fruit: ", copy_fruit)
print("fruit: ", fruit)

# fruit = ["apples", "bananas", "oranges"] (list of fruit)
# copy_fruit = fruit.copy() (creates a new list from fruit: copy)
# print("copy_fruit") printed the copy 
# copy_fruit.pop() #pops out the last value so (orenges will not show)
# print("copy_fruit: ", copy_fruit) 
# print("fruit: ", fruit) shows the original fruit list & the copy list that was made 

print("="*50) 

# copying a list with a full slice ___ list[:]

copy_fruit = fruit[:]
print(copy_fruit) # this is also a true copy 
copy_fruit.pop()
print("copy_fruit: ", copy_fruit)
print("fruit: ", fruit) # shows the original fruit list & the copy list that was made

print("="*50)

# list slicing: list[start:stop] ( you can get a secton of a list = slice) will return a sublist from the start index to the stop index, but not including the stop index
# the "stop" is not included - so if start index is 0 and stop index is 3, it will return the list from index 0 - 2 (will not include index 3)

fruit = ["apples", "bananas", "oranges", "grapes", "peaches"]
print("fruit sliced: ", fruit[1:4]) # will return ["bananas", "oranges", "grapes"]
print("fruit sliced: ", fruit[:4]) # will return ["apples", "bananas", "oranges", "grapes"]
print("fruit sliced: ", fruit[1:]) # will return ["bananas", "oranges", "grapes", "peaches"]
print("fruit sliced: ", fruit[::2]) # will return ["apples", "oranges", "peaches"] (every second item)

print("="*50)

#Indecies          0       1       2       3       4
key_lime_pie = ["slice1, slice2, slice3, slice4, slice5"]
#neg indecies     -5      -4      -3      -2      -1

my_slice = key_lime_pie[0:1]
print(my_slice) # will return ["slice1"]

big_slice = key_lime_pie[1:3]
print(big_slice) # will return ["slice2", "slice3"]

last_slice = key_lime_pie[4:]
print(last_slice) # will return ["slice5"]

another_slice = key_lime_pie[3:-1]
print(another_slice) # will return ["slice4"]

another_slice2 = key_lime_pie[-1:]
print(another_slice2) # will return ["slice5"]v

#list slicing: list[start:stop:step] (you can get a section of a list = slice)
another_slice4 = key_lime_pie[-1:-3:-1] # specifying a step parameter to tell python how to move unto the nextitem in the list 
print(another_slice4) # will return ["slice5", "slice4"]

print("="*50)

# joining a list together to form a single string with the ".join()" method

words = ["Hello", "I'm", "getting", "joined", "!!!!!"]
sentence = " ".join(words) 
print(sentence) # will return "Hello I'm getting joined!!!!!"

new_sentence = "****".join(words)

numbers = [1, 2, 3, 4, 5]
string_numbers = " ".join(str(numbers)) # converts numbers to strings and joins them with spaces
print(string_numbers) # will return "1 2 3 4 5"

print("="*50)







