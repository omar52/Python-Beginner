# Exceotions:
# is a way to handling the error in python

# try:
#     # some code lines
# except <ERROR1>:
#     # handler ERROR1
# except <ERROR2>:
#     # handler ERROR1
# except:
# else:
      # no exceptions were raised, the code ran successfully
# finally:
      # do something in any case

# try:
#     result = 2 / 0
# except ZeroDivisionError :
#     print('we can not divide by zero')
# finally:
#     result = 302

# print(result)


################ we can use raise Exception

try:
    raise Exception('an error')
except Exception as error:
    print('an error!')       # here it will not print the error message