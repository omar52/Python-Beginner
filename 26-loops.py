# while loop, it is used to define  code while there is a certain condition

# count = 0
# while count < 10:
#     print("the condition is true")
#     count += 1

# print("after the loop")

# For loop, it is generally used to iterate through a list 
# items = [1,2,3,4,5,6]
# for item in range(15):  # Range function returns a list from 0 to the number previous to the numb
#     print(item)

# to print the indexs of the items
items = [ "omar" , "abdallah" ,"mos"]
for index, item in enumerate(items): # enumerate => return a list of indexs and values => [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
    print(index, item)