# it is mutable, and like the dictionary but without keys
# there is immutable type which is called frozen sets
set1 = {"Omar", "Ali"}  
set2 = {"atef"}
print(set1 & set2)  # intersecting
print(set1 | set2)  # Union
print(set1 - set2)  # subtraction
print(set1 > set2)  # is set1 has all elemnts in set2 (is set2 is subset of set1)
print(list(set1))   # making a list of the set elements if the set has a dublication of an elemnt when it converted to list there is no dupplication appear

