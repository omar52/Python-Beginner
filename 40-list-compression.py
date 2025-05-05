number = [1,2,3,4,5,6]
numbers_power_2 = [round(n/3) for n in number]
print(numbers_power_2)


# in a loop

num = []
for n in number:
    num.append(round(n/3))
    
print(num)


# using map func:

new = (list(map(lambda n : round(n/3),number)))
print(new)