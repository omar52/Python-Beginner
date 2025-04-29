#You should use enum types any time you need to represent a fixed
# set of constants. That includes natural enum types such as the 
# planets in our solar system and data sets where you know all 
# possible values at compile time—for example, the choices on a menu, 
# command line flags, and so on. The output is: Mondays are bad.


# we must import Enum from enum library
from enum import Enum

# now we can initialize new Enum:
class State(Enum):
    INACTIVE = 0
    ACTIVE = 1
    
print(State.ACTIVE.value)
print(State(1).value)
print(State['ACTIVE'].value)
print(len(State))

print(list(State))