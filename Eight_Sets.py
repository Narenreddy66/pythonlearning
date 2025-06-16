# Add/Remove Set Items

# 1:add:if we want to add single elemtns 
# 2.update:if multiple eleemtns adding
a={"eleven","ewwew","wkekwes"}
a.update("wmwmw","qwkeke")
print(a)
# 3.remove
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)
# if do remove element which is no there in elemet then shows error then use discard
# 4.pop
# pop():This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.

# Example:

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)



# 5.del:
# del is not a method, rather it is a keyword which deletes the set entirely.

# Example:

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
  

# Output:

# NameError: name 'cities' is not defined

# We get an error because our entire set has been deleted and there is no variable called cities which contains a set.

# What if we don’t want to delete the entire set, we just want to delete all items within that set?

# 6.clear():
# This method clears all items in the set and prints an empty set.

# Example:

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)


# JOIN SETS

# union: in this it give new set 
vehicles={"car","bus","bike"}
citie = {"Tokyo", "Madrid", "Berlin", "Delhi"}
completeItems=vehicles.union(citie)
print(completeItems,"ccccccccccccccccccccccccccccc")

# update:it gives value in same set
vehicle={"car","bus","bike"}
citi = {"Tokyo", "Madrid", "Berlin", "Delhi"}
vehicle.update(citi)
print(vehicle)


# intersection() and intersection_update():
# The intersection() and intersection_update() methods print only items that are
#  similar to both sets. The intersection() method returns a new set whereas the
#  intersection_update() method updates the existing set from another set.
vehi={"car","bus","bike"}
cit = {"Tokyo", "Madrid", "Berlin", "Delhi","bike"}
newcites = vehi.intersection(cit)
vehi.intersection_update(cit)
print(newcites,"nnnnnnnnnnnnnnn")
print(vehi,'nneeeeeeeeeeeeeeeee')


# III. symmetric_difference() and symmetric_difference_update():
# The symmetric_difference() and symmetric_difference_update() methods print only items that are not similar to both sets. The symmetric_difference() method returns a new set whereas the symmetric_difference_update() method updates the existing set from another set.

# Example 1:

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
cities.symmetric_difference_update(cities2)
print(cities3,"symmmmmmmmmmmmmmm")
print(cities,"suuuuuuuuuuuuuu")



# IV. difference() and difference_update():
# The difference() and difference_update() methods print only items that are only present in the original set and not in both sets. The difference() method returns a new set whereas the difference_update() method updates the existing set from another set.

# Example 1:

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)


# SETMETHODS:
# 1.isdisjoint():
# The isdisjoint() method checks if items of a given set are present in another set. This method returns False if items are present, else it returns True.

# Example 1:

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))

# 2.• issuperset():
# The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.

# Example 1:

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Kabul"}
print(cities2.issuperset(cities3))

# 3.• issubset():
# The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.

# Example 1:

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))