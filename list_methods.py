# some cool things that we can do with list methods

food = ["tacos", "pizza", "tiramisu"]

print("Adding ice cream")
food.append("ice cream")
print(food)

# list.insert() --- method inserts an item at a specific index in the list
# what goes inside the parentheses are the index and the item we want to add

print("Inserting a potato into our list of food")
food.insert(2, "potato")
print(food)

food.insert(6, "cheeseburger") # index 6 does not exist but it will just add to the end of list
print(food) 

# list.pop() --- method removes and returns the last item from the list
# what goes inside the parentheses is the index of the item you want to remove
# just because the .pop() method also returns the value removed, doesnt mean we have to store it or use it

print("Putting our cheeesein the fridge")
fridge = food.pop()
print("What was in the fridge: ", fridge)
print(food)

print("="*50)

# list.pop(index) --- method removes and returns the item at the specified index from the list

print("Putting our potato in the oven")
fridge = food.pop(2)
print("Whats in the oven?: ", fridge)
print(food)

print(f"I really like {food[0]},I also love {food[1]}, and I'm obessed with {food[2]}") # we can access items by their index in the list
# this is a format string, it allows us to insert variables into a string from lists or other data structures

print("="*50)

# Hit up the grocery store
food.append("key line pie")
food.append("cheese burger")
food.append("fish")
food.append("sushi")
food.append("beer")
food.append("salad")

print("We went to the grocery store")
print(food)

# list.inndex(item) : will; return the index of a perticualar item in the list
print("finding the index of bee using .index()")
beer_idx = food.index("beer")
print("the indexical position of beer in our food list is: ", beer_idx)


print("="*50)

# modifying a data at a specific index/position: Mutability list[index] = new_item

print("change beer into juice?")
food[8] = "juice"
print(food)
food.append("cheese burger")

# list.count(item) : will return the number of times a particular item in the list and return a interger
burger_count = food.count("cheese burger")
print("Burger count: ", burger_count)


# list.reverse() : will reverse the order of items in the list
print("original food list: ", food)
food.reverse()
print("Our food list reversed: ",food)

print("="*50)

# list.sort() : will sort the items in the list in ascending order either alphabetically or numerically
# when sorting a list, all items within must be the same data type 

print("sorting our food list in alphabetical order")
food.sort()
print(food)

# list.reverse() : will reverse the order of items in the list
food.sort(reverse=True)
print(food)  

print("="*50)

# list functions
# len(item) : len = length : will return the number of items in the list
#len(item0 can be used in more then just list as well
print("Length of our food list: ", len(food))

# sum(item) : will return the sum of all the numbers in the list ( give us the sum total of all the numbers in a list)
# the list must be made up of entirely of numbers/intergers/floats

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
total = sum(nums)
print("the sum of all the nums in our list is : ", total)



