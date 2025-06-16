# Manipulating Tuples
# Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operations on that list and convert it back to a tuple.

# Example:

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       # add item 
temp.pop(3)                 # remove item
temp[2] = "Finland"         # change item
countries = tuple(temp)
print(countries)

# Unpack Tuples
# Unpacking is the process of assigning the tuple items as values to variables.
details=("suraj","12","vedham")
(name,age,school)=details
print("Nmae"+ ":" + name)
print("Age" +":" +age)
print("School" +":" +school)


# But what if we have more number of items than the variables?

# You can add an * to one of the variables and depending upon the position of the variable and number of items, Python matches variables to values and assigns them to the variables.

# Example 1:

fauna = ("cat", "dog", "horse", "pig", "parrot", "salmon")
(*animals,birds,plants)=fauna
print("Animlas"+":" ,animals)
print("Birds"+":" , birds)
print("plants" +":" ,plants)