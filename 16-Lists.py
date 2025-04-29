# list can include different data types and also can be empty
students = ["omar", "dyiaa", "ali" , "ayman"]
print("omar" in students)
# list is mutable
students[3] = "dodo"
print(students)
# print  certain elements from the array
print(students[0:4])
# define the list elements numbers  ==> elements nunber = las-index +1
print(len(students))


# the methods of string:
print("-----------------methods--------------")
# 1- adding elements to the last of the list ====>  append & extend $ += operators : add element to the last of the list
students.append("atef")      # add the element as it is 
students.extend(["ahmed"])   # it must be included in square brackets
students.extend({5})   # it must be included in square brackets
students += ["ali"]    # the same as the extend function
print(students)

#### an new way to form a list of any name characters :
name = []
name.extend("omar")  # = name += "omar"
print(name)

print(list("omar"))



# 2- Removing elements from list:
# 2.1 remove function
students.remove("omar")
print(f" the number is now {len(students)}")
students.remove("ali")
print(f" the number is now {len(students)}")
# 2.2 pop function  -- it removes the last element in the list
print(students.pop())
print(f" the number is now {len(students)}")
print(students)

# 3 - adding items to the specific index or position:
numbers = [0,1,2,3,4,5,6,7,8,9]
# 3.1 insert method: it add only one element and all the elements after the index get shifted 
numbers.insert(0,"omar")
print(numbers)
# 3.2 Slicig : it add multiple elements and all the elements after the index get shifted 
numbers[1:1] = ["numb1", " numb2"] # it means that it replace the elements from the index(1) to the index (1)  with the assigned elements
print(numbers)

