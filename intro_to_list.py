# Python Lists

# Lists are just collections of items. Mutable, ordered, dynamic

#-- Mutable : We have the ability to mutate lists; add, remove, manipulate data
#-- Ordered : Each item in a list has a specific position, which allows us to know where each item is (indecies/indexes)
#-- Dynamic : We can add and remove data from lists allowing them to grow and shrink as needed


# Lists are created with [] square brackets, and each item inside of a list is separated by a comma --> ,

# empty list
empty_list = []

# Populated list

person = 'Jill'

people = [person, 'Bob', "Barry", "Bill"]

# Python lists can contain many different data types

stuff = [12, 'apple', False, 3.14, ['Dylan', 'Travis', ['tacos']]]

#----- List Indecies

# Each item is marked by a specific index
# Indecies are in numeric order starting from 0, we can use them to access, modify, and remove items from our list

#indecies   0        1         2       3
alist = ['item1', 'item2', 'item3', 'item4']
print(alist)

# grab item 3 with index 2

print("third item: ", alist[2])

# grab the first item with index 0

print("Item 1, first item: ", alist[0])

# grab the last item with index 3

print("The last item: ", alist[3])

# grab the last item with negative index -1 ( if yu may not have a visual representaton of your list, remember that the last item is at index -1)

print("The last item accedded with index -1: ", alist[-1])

# grab the third item in alist with index -2
print("the list item accessd with index -2: ", alist[-2])

# potention pitfall 

# IndexError: list index out of range (the index doesnt exist in the list)

# print(alist[4]) # this will cause an IndexError in terminal - it will not stop the program, it will simply print an error message


