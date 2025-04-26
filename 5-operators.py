    # 1- Assign operator  (age = 25)
    
    # 2- arithmetic operators (math operators)
1+1  # 2 
2-1  # 1
2*2  # 4
4/2  # 2  
4%3  # 1  
4**2 # 16
# [+= , -=, *=, /=] 
print(17//3) # 5, it removes the decimal numbers 

# plus operator can be used to concatinate string values
print("Omar" + " is a good person")

    # 3- comparison operators
    
a = 1; b = 2
print(a == b); print(a != b); print(a > b); print(a<=b)

    # 4- Boolean operators [not, and, or]
    
condition1 = True
condition2 = False
print("=========== boolean operators ======")
print(not condition1); print(condition1 and condition2); print(condition2 or condition1) # this is considered an condition means that is the value is true???
# for or it returns the first value if it is not a falsy value
# for and it only evaluates/returns the second value if the first value is not falsy[false, zero ,empty list , empty string]

    # 5- bitwise operators very rare [& |]
    
    # 6- is & in operators
    # 7- Ternary operator

def is_adult(age):
    return True if age > 18 else False 

# # it is equal to :  if age > 18:
#                     return True
#                     else:
#                     return False

print("function_ Test"); print(is_adult(18.2))


