# sort method is used to sort the list, but all elements must be the same typ
# the sort method sorts only the upper case letters first and then the lower case letters
items = ["a",  "c", "d", "E", "f" ,"B"]
# items.sort()
# print(items)
# to fix the priority of upper cease letters ,we use the key
# items.sort(key=str.lower)  # or  items.sort(key=str.upper)
# print(items)

# the previous function will modifiy the original list , if I want to sort it without 
# modifing the original list i use general function called (sorted)
print(sorted(items, key=str.lower))
print(items)