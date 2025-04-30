# hello! function
def hello(name="my friend", age=5):
    print(f"hello, {name.title()}, you are {age} years")
hello("omar",35)
hello()

# Any change inside the function does not affect anything outside the function for immutable data like string and number
def change(value):
    value = 2
val = 1
change(val)
print(val)    # ==> dose not change
# but if we used dictionary or list who are mutable the data will change
def change(value):
    value["name"] = "omar"
val = {"name" : "Ali"}
change(val)   # ==> changed
print(val)

# Return Word
    # = it stops the block of codes

def hello(name):
    if not name:
        return
    print(f"hello, {name.title()}")
hello("")

    # = we can return more than onthing separated by commas

def hello(name):
    print(f"hello, {name.title()}")
    return name, "omar", {"name":"ALi"}
returned_value=hello("omar")
print(returned_value)