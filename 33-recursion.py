# in python it means that the function recall itself:
# the factorial example is the best

def factorial(a):
    if a == 1:
        return 1
    return 4 * factorial(a-1)

print(factorial(3))
print(factorial(4))
