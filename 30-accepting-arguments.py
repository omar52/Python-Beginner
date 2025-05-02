# Accepting arguments
# import sys
# name = sys.argv[1]
# print(f"hello {name}")   # from the comand line we can pass arguments and the result will be a list of the file name and all the aruments in string form

import argparse
parser = argparse.ArgumentParser(
    description='this program is ......'
)

parser.add_argument("-c", '--color', metavar ='color', required = True,
choices={'red',"blue"} , help = 'the color to search for')

args = parser.parse_args()

print(args.color)