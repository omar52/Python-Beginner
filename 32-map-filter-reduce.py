# three functions are global functions
from functools import reduce
# 1- map(): apply the function on all list items

numbers = [1, 2, 3]

double = lambda a : 2*a   # lambda function return the result by default

resutlt = map(double, numbers)
# print(list(resutlt))

# 2-filter(): it also iteratethe list elements and return a filter object
numbers = [1, 2, 3 , 16]

# def isEven(a):   # it must return true or false 
#     return a % 2 == 0    # the condition is true

resutlt2= filter(lambda a : a%2 ==0 , numbers)
print(list(resutlt2))


# reduce() : we must import it from functools 

expenses = [ 80, 100, 30,40,50]

# sum = 0
# for expense in expenses:
#     sum += expense[1]

sum = reduce(lambda a, b : a + b ,expenses)

print(sum) 
