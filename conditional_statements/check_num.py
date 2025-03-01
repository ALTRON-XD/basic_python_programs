# write a python program to check if a num is +ve, -ve or 0
i = int(input("enter num;")) # taking input number from user
if i > 0: # conditon for positive
    print("+ve") 
elif i < 0:  # conditon for negative
    print("negative")
else:
    print("zero")
