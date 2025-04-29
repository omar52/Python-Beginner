# dictionary name = { "key" : any data type }

student = {"name" : "omar", "job" : "TA"}        # How to write down the dictionary
## How to acess to any data in Dictionary
# 1- Notation method
print(student["name"])

# 2- get method   , if it is not found it return none
print(student.get("job"))
print(student)

## How to delete an item:
# 1- pop method: remove the written value
print(student.pop("name"))
del student["job"]
print(student)
# 2- popitem method: remove the last
student["name"] ="omar"
print(student)
print(student.popitem())
print(student)
student["name"] ="omar"

# 3- check if there is a key in the dictionary
print("job" in student)
# 4- getting a list of the dictionary keys
print(list(student.keys()))
# 5- getting a list of the dictionary values
print(list(student.values()))
# 6- convert the dictioanry to a list of tuples pairs
print(list(student.items()))
# 7- define the length of the dictionary (no of pairs)
print(len(student))
# 8- add new "value" : "key" to the dictionary
student["nick-name"] = "Dyiaa"
print(student)
# 9- make a copy of the dictionary
new_student = student.copy()
print(new_student)