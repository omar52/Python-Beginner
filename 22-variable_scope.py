# the declaration place of the variable is important for how the code see this var
# 1- if it is in the global it will bee seen by all code after the declaration

age = 8
def test():
    print(age)

print(age)
test()

# 2- if it is located inside the function, it will be in local location

# def test():
#     age = 8
#     print(age)

# # print(age) # it will give an error as it dose not see what is inside
# test()