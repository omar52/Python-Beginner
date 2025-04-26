# class ==> bool type
# boolean values can be used as condition in conditional statement
# All numbers are considered true except 0
# string  is considered false if empty , it it has space it is not empty
# tuples, sets, and lists are false if they are empty 
# falsy values ===>>> [0, False, [], {}, ""]

done = {}

if done:
    print("yes")
else:
    print("No")
    

# any Global function:

book_read1 = False
book_read2 = False

read_any_book = any([book_read1,book_read2])  # works as or operator
read_all_book = all([book_read1,book_read2])  # works as and operator
print(read_any_book)
    