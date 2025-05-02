from hi import hello
hello()

# there sre two types of importing modules:
# 1- import the file name itself  import dog ---> gog.hello()
# 2- import the function from the file ---> from filename.py or import func.name
# if the file is existed in more levels --> from file-one.function-file import function-name

########### python standard libraries:
# math for math utilities
# re for regular expression
# json to work with JSON
# datetime to work with dates
# sqlite3 to use SQLite
# os for Operating System Utilites
# random for random number generation
# statistics for statistics utilities
# requests to perform HTTP network requests
# http to create HTTP servers
# urllib to mangae URLs

## EXAMPLe
import math

print(round(math.sqrt(30)))