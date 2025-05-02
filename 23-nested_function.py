# nested functions:
def count():
    count = 0
    
    def increment():
        nonlocal count    # to acess a variable in the outerfunction we should put nonlocal
        count = count + 1
        print(count)
    
    increment()
    
count()