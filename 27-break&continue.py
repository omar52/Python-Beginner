# Both loops (for and while) can be interrupted using block and continue
# 1- continue stops the current iteration
    # items = [0,1,3,4,5,2,6]
    # for item in items:
    #     if item == 2:
    #         continue
    #     print(item)
    
# 2- break stops the loop altoghter 
items = [0,1,3,4,5,2,6]
for item in items:
    if item == 2:
        break
    print(item)