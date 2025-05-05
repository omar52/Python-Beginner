# with statement is useful for automatically colse the files after opening them:
filename = '/Users/Omar/tes.txt'

# try:
#     file = open(filename , 'r')
#     content = file.read()
#     print(content)
# finally:
#     file.close()

with open(filename, 'r') as file:
    content = file.read()
    print(content)
    
    # here the file is closed automatically