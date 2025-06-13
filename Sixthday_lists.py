# Add List Items
# append():
# This method appends items to the end of the existing list.

# Example:
colors = ["voilet", "indigo", "blue"]
colors.append("mamsms")
print(colors)

# insert():
# This method inserts an item at the given index. The user has to specify the index and the item to be inserted within the insert() method.

# Example:

colors = ["voilet", "indigo", "blue"]
colors.insert(1,"3k3eoe3ko")
print(colors)

# extend():
# This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.

# Example 1:

# add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = {"green", "yellow", "orange", "red"}
colors.extend(rainbow)
print(colors)

# Concatenate two lists:
# You can simply concatenate two lists to join them.

# Example:

colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)

# Remove List Items
# There are various methods to remove items from the list: pop(), remove(), del, clear()
#1. pop:deltes the last elemt and if give particular index delete that
colors = ["voilet", "indigo", "blue"]
colors.pop()
colors.pop(1)
print(colors)

# 2.remove:delete specific element
colors = ["voilet", "indigo", "blue"]

colors.remove("blue")
print(colors)

# 3.del: is not method 
# delette emtire lst or specfifc index
colors = ["voilet", "indigo", "blue"]
del colors[1]
print(colors)

# 4.clear():
# This method clears all items in the list and prints an empty list.

# Example:

colors = ["voilet", "indigo", "blue", "green", "yellow"]
colors.clear()
print(colors)


# Change List Items
# Changing items from a list is easier; you just have to specify the index where you want to replace the item with an existing item.

# Example:

names = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
names[2] = "Millie"
print(names)

# List Comprehension
# List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.

# Syntax:

# List = [expression(item) for item in iterable if condition]

# expression: it is the item which is being iterated.
# iterable: it can be list, tuples, dictionaries, sets, and even in arrays and strings.
# condition: condition checks if the item should be added to the new list or not.
# Example 1: accepts items with the small letter “o” in the new list

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)






# LISTMETHODS
# 1.Sort:Arranges in Ascending orders
a=[1,2,23,9,28,4,6,10]
a.sort()
print(a)
# descending:reverese=true
colors = ["voilet", "indigo", "blue", "green"]
colors.sort(reverse=True)
print(colors)

# 2.reverse(): This method reverses the order of the list.
colors = ["voilet", "indigo", "blue", "green"]
colors.reverse()
print(colors)

# 3.index(): This method returns the index of the first occurrence of the list item.
colors = ["voilet", "indigo", "blue", "green"]
print(colors.index("blue"))

# 4.count(): Returns the count of the number of items with the given value.
# Example:

colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.count("green"))

# 5.copy(): Returns a copy of the list. This can be done to perform operations on the list without modifying the original list.
# Example:

colors = ["voilet", "green", "indigo", "blue"]
newlist = colors.copy()
print(colors)
print(newlist)