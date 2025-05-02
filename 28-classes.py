# classes are type of python data type, and from them we can instantiate object 
# an object is an instance of a class, a class is a type of object

class Parents:        # We created this class to apply the inhertance from it tho the below class
    def walk(self):
        print("walking.........")

class Student(Parents):    # To create a class, we just put word class besides to class name
     def __init__(self, name, age): # here we add a special type of method called instructor using word __inite__ we use this constructor to initalize one more properties when we create a new object
        self.name = name
        self.age = age
     
     def saluate(self):  # I added a method to the class
       print("hey!")
      

# omar = Student()  # here i created object from the class without any properties
omar = Student("omar" , 27)  # here i created object from the class additional any properties
print(f"hello {omar.name}, you are {omar.age}")
omar.saluate()
omar.walk()     # this method is herited from parent class 