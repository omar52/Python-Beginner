#there are several data types 

print("------string-----")
name = "omar"; print(type(name)); print(type(name) == str); print(isinstance(name, str)); print("------intger---------")   # string type

# number:

age = 2; print(isinstance(age,int)); print(type(age));print("----float----") #intger number type
age2 = 2.8; print(isinstance(age2,float)); print(type(age2)) #float number type

# We can convert int to float through float function and the vice versus
print("converting int to float")
print(float(age))
print(int(age2))  # it make a round to the lowest whole number 
print(int("25"))

# other data types:
# class    for types
# 1- complex for complex number
# 2- bool for booleans
# 3- list for lists
# 4- tuple for tuples
# 5- range for ranges
# 6- dict for dictionaries
# 7- set for sets