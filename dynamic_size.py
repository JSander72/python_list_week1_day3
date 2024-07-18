# dynamic means our list can grow and shrink as needed by adding and removing items

bec_class = ["David", "James", "Adam", "Tyler"]
print(bec_class)

# adding to list

# list.append() --- method adds an item to the END of the list 
# what goes inside the parentheses is the item we want to add

bec_class.append("Vincent")
print(bec_class)

bec_class.append("Vincent")
print(bec_class)

bec_class.append("Emily", "Emily", "Emily") # you can only appennd one item at a time

# removing from list
# list.remove() --- method removes the first occurrence of an item from the list
# what goes inside the parentheses is the item we want to remove

bec_class.remove("Adam")
print(bec_class)

bec_class.remove("Vencent") # will only remove the first occurrence of "Vincent" not all that match
print(bec_class)






