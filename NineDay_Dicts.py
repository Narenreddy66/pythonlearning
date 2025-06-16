info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])
# print(info.get('eligible'))
# for key in info.keys():
#     print(key,"ddddddddddddddddddddddddddddd",info[key])
for key ,value in info.items():
    print("hii" ,key,value)


    # Add/Remove Items
#    1. Adding items to a dictionary:
info = {'name': 'Karan', 'age': 19, 'eligible': True}
print(info)
info["naren"]="Narendhar"
print(info)
# update
info = {'name': 'Karan', 'age': 19, 'eligible': True}
print(info)
info.update({'age': 20})
info.update({'DOB': 2001})
print(info)



# 2.Removing items from dictionary:

# clear():
# The clear() method removes all the items from the dictionary.

# Example:

info = {'name': 'Karan', 'age': 19, 'eligible': True}
info.clear()
print(info)

# pop():
# The pop() method removes the key-value pair whose key is passed as a parameter.

# Example:

info = {'name': 'Karan', 'age': 19, 'eligible': True}
info.pop('eligible')
print(info)

# popitem():
# The popitem() method removes the last key-value pair from the dictionary.

# Example:

info = {'name': 'Karan', 'age': 19, 'eligible': True, 'DOB': 2003}
info.popitem()
print(info)