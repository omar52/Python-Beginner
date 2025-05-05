# decorator is assigned to function through @decorator-name
# whenever we call the function the decorator is going to be called 
# decoratr takes a nction as a parameter wrapps the function in inner function

def logtime(func):
    def wrapper():
        print("before")
        val = func()
        print("after")
    return wrapper    # must be returned here
@logtime
def hello():
    print('hello Omar')
    
hello()